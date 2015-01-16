#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys ##sysをインポートしないと12行目のsys.exit()が成り立たない

##from jp.ac.kyoto_su.cse.pl.Bodies.Example import Example as example ##from メインまでのファイルまでの道のり import Exampleファイル
import jp.ac.kyoto_su.cse.pl.Bodies.Example ##総理大臣の書き方で


if __name__ == '__main__':
	an_example =jp.ac.kyoto_su.cse.pl.Bodies.Example.Example()##importまでの道のり.クラス呼び出し
	sys.exit(an_example.main())##sys.exit([arg]) pythonの終了
