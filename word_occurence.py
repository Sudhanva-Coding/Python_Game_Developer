from collections import Counter
import re

text = "In 771 BCE, a Quanrong invasion in coalition with the states of Zeng and Shen — the latter polity being the fief of the grandfather of the disinherited crown prince Yijiu — destroyed the Western Zhou capital Haojing, killing King You and establishing Yijiu as king at the eastern capital Luoyi (雒邑).[4] The event ushered in the Eastern Zhou dynasty, which is divided into the Spring and Autumn and the Warring States periods. During the Spring and Autumn period, China's feudal system of fengjian (封建) became largely irrelevant. The Zhou court, having lost its homeland in the Guanzhong region, held nominal power, but had real control over only a small royal demesne centered on Luoyi. During the early part of the Zhou dynasty period, royal relatives and generals had been given control over fiefdoms in an effort to maintain Zhou authority over vast territory.[5] As the power of the Zhou kings waned, these fiefdoms became increasingly independent states."

words = re.findall("\w+", text )
print(Counter(words).most_common(10))
