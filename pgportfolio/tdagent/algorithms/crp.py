from ..tdagent import TDAgent
import numpy as np


class CRP(TDAgent):
    """ Constant rebalanced portfolio = use fixed weights all the time. Uniform weights are commonly used as a benchmark.

    Reference:
        T. Cover. Universal Portfolios, 1991.
        http://www-isl.stanford.edu/~cover/papers/paper93.pdf
    """

    def __init__(self, b=None):
        """
        :params b: Constant rebalanced portfolio weights. Default is uniform.
        """
        super(CRP, self).__init__()
        self.b = b

    def decide_by_history(self, x, last_b):
        # print(x.shape)
        x = self.get_last_rpv(x)

        # init b to default if necessary
        #2022.02.21修改
        # if self.b is None:
        #     self.b = np.ones(len(x)) / len(x)
        #强制不配现金
        # if self.b is None:
        #     self.b = np.ones(len(x)) / (len(x)-1)
        #     self.b[0]=0
        #2022.02.27 22:14现在强制不配现金了。所以也没必要少一环了，直接恢复初始状态即可
        if self.b is None:
            self.b = np.ones(len(x)) / len(x)
        return self.b

