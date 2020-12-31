# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(1)

# 별칭
# import theater_module as mv
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

# *
# from theater_module import *
# price(3)
# price_soldier(3)
# price_morning(3)

# 특정 함수만 지정
# from theater_module import price, price_morning
# price(3)
# # price_soldier(3)
# price_morning(3)

# 특정 함수만 지정하고 별칭 지정
from theater_module import price_soldier as price
price(3)