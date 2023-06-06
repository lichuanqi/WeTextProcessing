import time
from tn.chinese.normalizer import Normalizer
from itn.chinese.inverse_normalizer import InverseNormalizer

text_tn = '13路34563部队'
text_itn = '郊区一教育十一路三四五六三部队中建三局四公司'

# TN
print('TN初始化开始')
t_start = time.time()
normalizer = Normalizer(
    cache_dir="tn",
    # overwrite_cache=True,
)
t_end = time.time()
print('初始化完成，用时: %.3f'%(t_end-t_start))

t_start = time.time()
rsl = normalizer.normalize(text_tn)
t_end = time.time()
print('预测完成, 用时: %.3f, 结果: %s'%(t_end-t_start, rsl))

# ITN
print('TN初始化开始')
t_start = time.time()
invnormalizer = InverseNormalizer(
    cache_dir="itn",
    overwrite_cache=True
)
t_end = time.time()
print('初始化完成，用时: %.3f'%(t_end-t_start))

t_start = time.time()
rsl = invnormalizer.normalize(text_itn)
t_end = time.time()
print('预测完成, 用时: %.3f, 结果: %s'%(t_end-t_start, rsl))