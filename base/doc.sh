case $1 in
#  code doc 
  'git') w3m https://segmentfault.com/a/1190000000307435;;
  'gitee') w3m https://www.gitee.com;;
  'docker') w3m https://docker.com;;
  'nginx')w3m http://tengine.taobao.org/book/index.html;;
  'python') w3m https://www.runoob.com/python3/python3-data-analysis.html;;
  'ceph') w3m https://docs.ceph.com/en/latest/ ;;

# blog doc
  'hexo') w3m https://hexo.io/zh-cn/docs/configuration;;
  'next') w3m https://theme-next.js.org/docs;;
  'weixin') w3m https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html;;
  'weechat') w3m https://weechat.org/doc/;;

# other website
  'stock') w3m https://www.eastmoney.com ;;
  'phone') w3m http://www.shoujixiufu.com/;;
  'penpai') w3m https://www.thepaper.cn/;;
  'bing') w3m http://www.bing.com;;
  'dida') w3m https://www.dida365.com/webapp/;;
  'read') w3m https://weread.qq.com/;;
  
  *) echo -e 'input not match:  
  gitee / docker / nginx / python
  hexo / next / weixin
  stock / weechat / phone / penpai / bing / dida / read'
esac

  # case 'ps':
  #     url = "https://ps.gaoding.com/#/"
  # case 'dida':
  #     url = 'https://www.dida365.com/webapp/'

# https://github.com/pandao/editor.md
