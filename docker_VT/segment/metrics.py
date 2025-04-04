# YOLOv5 🚀 by Ultralytics, AGPL-3.0 license
"""
Model validation metrics
"""
#import sys
import numpy as np

#sys.path.append('../../segment')

from ..metrics import ap_per_class
#from val import nt as inst

def fitness(x):
    # Model fitness as a weighted combination of metrics
    w = [0.0, 0.0, 0.1, 0.9, 0.0, 0.0, 0.1, 0.9]
    return (x[:, :8] * w).sum(1)


def ap_per_class_box_and_mask(
        tp_m,
        tp_b,
        conf,
        pred_cls,
        target_cls,
        plot=False,
        save_dir='.',
        names=(),
):
    """
    Args:
        tp_b: tp of boxes.
        tp_m: tp of masks.
        other arguments see `func: ap_per_class`.
    """
    results_masks = ap_per_class(tp_m,
                                 conf,
                                 pred_cls,
                                 target_cls,
                                 plot=plot,
                                 save_dir=save_dir,
                                 names=names,
                                 prefix='Mask')[2:]

    results = {
        'masks': {
            'p': results_masks[0],
            'r': results_masks[1],
            'ap': results_masks[3],
            'f1': results_masks[2],
            'ap_class': results_masks[4]}}
    return results


class Metric:

    def __init__(self) -> None:
        self.p = []  # (nc, )
        self.r = []  # (nc, )
        self.f1 = []  # (nc, )
        self.all_ap = []  # (nc, 10)
        self.ap_class_index = []  # (nc, )

    @property
    def ap50(self):
        """AP@0.5 of all classes.
        Return:
            (nc, ) or [].
        """
        return self.all_ap[:, 0] if len(self.all_ap) else []

    @property
    def ap(self):
        """AP@0.5:0.95
        Return:
            (nc, ) or [].
        """
        return self.all_ap.mean(1) if len(self.all_ap) else []

    @property
    def mp(self):
        """mean precision of all classes.
        Return:
            float.
        """
        return self.p.mean() if len(self.p) else 0.0

    @property
    def mr(self):
        """mean recall of all classes.
        Return:
            float.
        """
        return self.r.mean() if len(self.r) else 0.0

    @property
    def map50(self):
        """Mean AP@0.5 of all classes.
        Return:
            float.
        """
        return self.all_ap[:, 0].mean() if len(self.all_ap) else 0.0

    @property
    def map(self):
        """Mean AP@0.5:0.95 of all classes.
        Return:
            float.
        """
        return self.all_ap.mean() if len(self.all_ap) else 0.0

    def mean_results(self):
        """Mean of results, return mp, mr, map50, map"""
        return (self.mp, self.mr, self.map50, self.map)
    

    #def mean_results(self, inst):
    #    """Mean of results, return mp, mr, map50, map"""
    #    weighted_ap50 = [(inst[i] * ap50) for i, ap50 in enumerate(self.ap50)]
    #    return (self.mp, self.mr, sum(weighted_ap50) / inst.sum(), self.map)

    def class_result(self, i):
        """class-aware result, return p[i], r[i], ap50[i], ap[i]"""
        return (self.p[i], self.r[i], self.ap50[i], self.ap[i])

    def get_maps(self, nc):
        maps = np.zeros(nc) + self.map
        for i, c in enumerate(self.ap_class_index):
            maps[c] = self.ap[i]
        return maps
    
    def f1_score(self):
        return self.f1    

    def update(self, results):
        """
        Args:
            results: tuple(p, r, ap, f1, ap_class)
        """
        p, r, all_ap, f1, ap_class_index = results
        self.p = p
        self.r = r
        self.all_ap = all_ap
        self.f1 = f1
        self.ap_class_index = ap_class_index




class Metrics:
    """Metric for boxes and masks."""

    def __init__(self) -> None:
       
        self.metric_mask = Metric()

    def update(self, results):
        """
        Args:
            results: Dict{'boxes': Dict{}, 'masks': Dict{}}
        """
        
        self.metric_mask.update(list(results['masks'].values()))

    def mean_results(self):
        return self.metric_mask.mean_results()

    def class_result(self, i):
        return self.metric_mask.class_result(i)

    def get_maps(self, nc):
        return self.metric_mask.get_maps(nc)

    def f1_score(self):
        return self.metric_mask.f1_score()
    
    @property
    def ap_class_index(self):
        return self.metric_mask.ap_class_index

    


KEYS = [
    
    'train/seg_loss',  # train loss
    'train/obj_loss',
    'train/cls_loss',
    'metrics/precision(M)',
    'metrics/recall(M)',
    'metrics/mAP_0.5(M)',
    'metrics/mAP_0.5:0.95(M)',  # metrics
    'val/seg_loss',  # val loss
    'val/obj_loss',
    'val/cls_loss',
    'x/lr0',
    'x/lr1',
    'x/lr2', ]

BEST_KEYS = [
    'best/epoch',
    'best/precision(M)',
    'best/recall(M)',
    'best/mAP_0.5(M)',
    'best/mAP_0.5:0.95(M)', ]