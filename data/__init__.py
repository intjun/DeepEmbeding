import torchvision.transforms as T

from .classify.ClassifyData import my_collate_fn,Street2shop
from .n_pair_mc.npair_dataset import EbayDataset
from .margin_cub200.cub200_margin import CUB200DataSet
from .mxdata.mxcub200 import cub200_iterator
from .mxdata.online_products import MxEbay
from .mxdata.online_products import getEbayData
from .mxdata.mxcub_simple import getCUB200