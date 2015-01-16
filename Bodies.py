#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys ##sysをインポートしないとsys.exit()が成り立たない

import jp.ac.kyoto_su.ac.cse.pl.Bodies.Example ##総理大臣の書き方でmain()までの道のり


if __name__ == '__main__':
	an_example =jp.ac.kyoto_su.ac.cse.pl.Bodies.Example.Example()##importまでの道のり.クラス呼び出し
	sys.exit(an_example.main())##sys.exit([arg]) pythonの終了
