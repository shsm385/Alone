#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup ##変更なし

setup(
	name='Bodies',##パッケージの名前を参照
	version='1.0.0',##アプリケーションのバージョン
	author='AOKI Atsushi',##パッケージの作者
	author_email='atsushi@cc.kyoto-su.ac.jp',##パッケージ作者の電子メールアドレス
	url='http://www.cc.kyoto-su.ac.jp/~atsushi/',##パッケージのホームページ
	description='Bodies written by Python and PyOpenGL',##パッケージについての簡単な概要説明
	long_description='ドラゴン・スズメバチ・うさぎ・ペンギン・鬼・赤ちゃんを3次元描画する',##パッケージについての詳細な説明
	  ##license='GNU Affero General Public License',##パッケージのライセンス
	platforms='OS X (10.10.1)',##プラットフォームのリスト
	  ##packages=['jp'],##参照ファイル
)
