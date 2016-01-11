# 安装lxml失败如何解决(OSX 10.11.2)
> 安装web时候发现报错，仔细查找了一下，原来是lxml没有安装，实践了一下，xCode install的方法不一定有效
> 所以改成这个方式，原文在[cannot-install-lxml-on-mac-os-x-10-9](http://stackoverflow.com/questions/19548011/cannot-install-lxml-on-mac-os-x-10-9)

```bash
 gosber@localhost  ~  brew install libxml2  
==> Downloading https://homebrew.bintray.com/bottles/libxml2-2.9.3.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libxml2-2.9.3.el_capitan.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/libxml2/lib
    CPPFLAGS: -I/usr/local/opt/libxml2/include

==> Summary
🍺  /usr/local/Cellar/libxml2/2.9.3: 275 files, 9.8M
 gosber@localhost  ~  brew install libxslt
==> Downloading https://homebrew.bintray.com/bottles/libxslt-1.1.28_1.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libxslt-1.1.28_1.el_capitan.bottle.tar.gz
==> Caveats
To allow the nokogiri gem to link against this libxslt run:
  gem install nokogiri -- --with-xslt-dir=/usr/local/opt/libxslt

This formula is keg-only, which means it was not symlinked into /usr/local.

OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/libxslt/lib
    CPPFLAGS: -I/usr/local/opt/libxslt/include


If you need Python to find bindings for this keg-only formula, run:
  echo /usr/local/opt/libxslt/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/libxslt.pth
  mkdir -p /Users/gosber/Library/Python/2.7/lib/python/site-packages
  echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/gosber/Library/Python/2.7/lib/python/site-packages/homebrew.pth
==> Summary
🍺  /usr/local/Cellar/libxslt/1.1.28_1: 145 files, 3.0M
 gosber@localhost  ~  brew link libxml2 --force
Linking /usr/local/Cellar/libxml2/2.9.3... 17 symlinks created
 gosber@localhost  ~  brew link libxslt --force
Linking /usr/local/Cellar/libxslt/1.1.28_1... 22 symlinks created
 gosber@localhost  ~  pip3.5 install lxml                                                                                              
Collecting lxml
  Using cached lxml-3.5.0.tar.gz
Installing collected packages: lxml
  Running setup.py install for lxml

Successfully installed lxml-3.5.0
```

## 干正事
> 才想起来是为了安装scrapy
```bash
gosber@localhost  ~  pip3.5 install scrapy
Collecting scrapy
  Using cached Scrapy-1.0.4.tar.gz
Requirement already satisfied (use --upgrade to upgrade): Twisted>=10.0.0 in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from scrapy)
Requirement already satisfied (use --upgrade to upgrade): w3lib>=1.8.0 in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from scrapy)
Requirement already satisfied (use --upgrade to upgrade): queuelib in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from scrapy)
Requirement already satisfied (use --upgrade to upgrade): lxml in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from scrapy)
Collecting pyOpenSSL (from scrapy)
  Using cached pyOpenSSL-0.15.1-py2.py3-none-any.whl
Collecting cssselect>=0.9 (from scrapy)
  Using cached cssselect-0.9.1.tar.gz
Requirement already satisfied (use --upgrade to upgrade): six>=1.5.2 in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from scrapy)
Collecting service-identity (from scrapy)
  Using cached service_identity-14.0.0-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): zope.interface>=4.0.2 in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from Twisted>=10.0.0->scrapy)
Collecting cryptography>=0.7 (from pyOpenSSL->scrapy)
  Using cached cryptography-1.1.2-cp35-cp35m-macosx_10_6_intel.whl
Collecting characteristic>=14.0.0 (from service-identity->scrapy)
  Using cached characteristic-14.3.0-py2.py3-none-any.whl
Collecting pyasn1-modules (from service-identity->scrapy)
  Using cached pyasn1_modules-0.0.8-py2.py3-none-any.whl
Collecting pyasn1 (from service-identity->scrapy)
  Using cached pyasn1-0.1.9-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): setuptools in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/setuptools-18.4-py3.5.egg (from zope.interface>=4.0.2->Twisted>=10.0.0->scrapy)
Collecting cffi>=1.1.0 (from cryptography>=0.7->pyOpenSSL->scrapy)
  Using cached cffi-1.4.2-cp35-cp35m-macosx_10_6_intel.whl
Collecting idna>=2.0 (from cryptography>=0.7->pyOpenSSL->scrapy)
  Using cached idna-2.0-py2.py3-none-any.whllug
Collecting pycparser (from cffi>=1.1.0->cryptography>=0.7->pyOpenSSL->scrapy)
  Using cached pycparser-2.14.tar.gz
Installing collected packages: pyasn1, pycparser, cffi, idna, cryptography, pyOpenSSL, cssselect, characteristic, pyasn1-modules, service-identity, scrapy
  Running setup.py install for pycparser
  Running setup.py install for cssselect
  Running setup.py install for scrapy
Successfully installed cffi-1.4.2 characteristic-14.3.0 cryptography-1.1.2 cssselect-0.9.1 idna-2.0 pyOpenSSL-0.15.1 pyasn1-0.1.9 pyasn1-modules-0.0.8 pycparser-2.14 scrapy-1.0.4 service-identity-14.0.0
```
