# coding:utf-8

from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar('第一张图标', '副标题')
bar.add("服装", ["衣服", "鞋子", "袜子", "帽子", "眼镜"], [2, 4, 15, 6, 23], is_more_utils=True)
# bar.print_echarts_options()
# bar.render('template/index.html')

line = Line('第一张图标', '副标题')
line.add("服装", ["衣服", "鞋子", "袜子", "帽子", "眼镜"], [2, 4, 15, 6, 23], is_convert=True)

env = create_default_environment('html')

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
