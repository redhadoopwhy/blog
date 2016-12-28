#coding=utf-8
import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()  # 自定义filter时必须加上


@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def custom_markdown(value):
    extensions = ["nl2br","extra","abbr","attr_list","def_list","tables","fenced_code","footnotes","smart_strong","admonition","smarty","meta","sane_lists","wikilinks",]
    return mark_safe(markdown.markdown(force_unicode(value),
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False,
                                       ))
