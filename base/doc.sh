command='lynx'
case $1 in
#  code doc 
  'git') $command https://segmentfault.com/a/1190000000307435;;
  'gitee') $command https://www.gitee.com;;
  'docker') $command https://docker.com;;
  'nginx')$command http://tengine.taobao.org/book/index.html;;
  'python') $command https://www.runoob.com/python3/python3-data-analysis.html;;
  'api') $command https://wiki.termux.com/wiki/Termux:API ;;
  # 'ceph') $command https://docs.ceph.com/en/latest/ ;;
  'ceph') $command https://tracker.ceph.com/projects/cephfs/issues;;
  'redis') $command https://redis.io/docs/;;
  'nodejs') $command https://nodejs.org/zh-cn/learn/getting-started/introduction-to-nodejs;;
  'daos')  $command https://docs.daos.io/v2.4 ;;
  
# blog doc
  'hexo') $command https://hexo.io/zh-cn/docs/configuration;;
  'next') $command https://theme-next.js.org/docs;;
  'weixin') $command https://developers.weixin.qq.com/doc/offiaccou nt/Getting_Started/Overview.html;;
  '$command') $command https://$command.org/doc/;;
  'wanfang') $command https://c.wanfangdata.com.cn/patent;;
  'io500') $command https://io500.org/;;
  'sqlite') $command https://www.runoob.com/sqlite/sqlite-tutorial.html;;

# other website
  'stock') $command https://www.eastmoney.com ;;
  'phone') $command http://www.shoujixiufu.com/;;
  'penpai') $command https://www.thepaper.cn/;;
  'bing') $command http://www.bing.com;;
  'dida') $command https://www.dida365.com/webapp/;;
  'read') $command https://weread.qq.com/;;
  
  *) echo -e 'input not match:
  gitee / docker / nginx / python / nodejs / ceph / daos / api
  hexo / next / weixin / weechat / wanfang / sqlite / io500
  stock / phone / penpai / bing / dida / read'
esac

  #   # 
  # case 'ps':
  #     url = "https://ps.gaoding.com/#/"
  # case 'dida':
  #     url = 'https://www.dida365.com/webapp/'

# https://github.com/pandao/editor.md
