import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 路由 as 北向路由
from ..命令行接口 import 路由 as 南向路由
from . import 接口 as 实现接口
#常量
ca代码4 = {
	"L": 北向路由.E路由类型.e本地,	#local
	"C": 北向路由.E路由类型.e直连,	#connected
	"S": 北向路由.E路由类型.e静态,	#static
	"R": 北向路由.E路由类型.e路由信息协议,	#RIP
	"M": 北向路由.E路由类型.e移动,	#mobile
	"B": 北向路由.E路由类型.e边界网关协议,	#BGP
	"D": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP
	"EX": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP external
	"O": 北向路由.E路由类型.e开放最短路径优先,	#OSPF
	"IA": 北向路由.E路由类型.e开放最短路径优先,	#OSPF inter area
	"N1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA external type 1
	"N2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA external type 2
	"E1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF external type 1
	"E2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF external type 2
	"i": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS
	"su": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS summary
	"L1": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS level-1
	"L2": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS level-2
	"ia": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS inter area
	"U": 北向路由.E路由类型.e静态,	#per-user static route
	"o": 北向路由.E路由类型.e按需路由,	#ODR
	"P": 北向路由.E路由类型.e静态,	#periodic downloaded static route
	"H": 北向路由.E路由类型.e下一跳解析协议,	#NHRP
	"l": 北向路由.E路由类型.e定位与身份分离协议	#LISP
}
ca代码6 = {
	"L": 北向路由.E路由类型.e本地,	#Local
	"LC": 北向路由.E路由类型.e本地,	#
	"C": 北向路由.E路由类型.e直连,	#Connected
	"S": 北向路由.E路由类型.e静态,	#Static
	"U": 北向路由.E路由类型.e静态,	#Per-user Static route
	"B": 北向路由.E路由类型.e边界网关协议,	#BGP
	"R": 北向路由.E路由类型.e路由信息协议,	#RIP
	"H": 北向路由.E路由类型.e下一跳解析协议,	#NHRP
	"IS": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS summary
	"I1": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS L1
	"I2": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS L2
	"IA": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS interarea
	"D": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP
	"EX": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP external
	"ND": 北向路由.E路由类型.e邻居发现协议,	#ND Default
	"NDp": 北向路由.E路由类型.e邻居发现协议,	#ND Prefix
	"DCE": 北向路由.E路由类型.e邻居发现协议,	#Destination
	"NDr": 北向路由.E路由类型.e邻居发现协议,	#Redirect
	"O": 北向路由.E路由类型.e开放最短路径优先,	#OSPF Intra
	"OI": 北向路由.E路由类型.e开放最短路径优先,	#OSPF Inter
	"OE1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF ext 1
	"OE2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF ext 2
	"ON1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA ext 1
	"ON2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA ext 2
	"l": 北向路由.E路由类型.e定位与身份分离协议	#LISP
}
ca协议字符串 = {
	北向路由.E路由类型.e直连: "connected",
	北向路由.E路由类型.e静态: "static",
	北向路由.E路由类型.e路由信息协议: "rip",
	北向路由.E路由类型.e开放最短路径优先: "ospf",
	北向路由.E路由类型.e增强内部网关路由协议: "eigrp",
	北向路由.E路由类型.e中间系统到中间系统: "isis",
	北向路由.E路由类型.e边界网关协议: "bgp"
}
#函数
def f生成显示路由表命令(a版本, *a参数, a虚拟路由转发 = None):
	v命令 = 命令.C命令("show")
	if a版本 == 协议.E协议.e网络协议4:
		v命令 += "ip"
	elif a版本 == 协议.E协议.e网络协议6:
		v命令 += "ipv6"
	for v参数 in a参数:
		if v参数 in 北向路由.E路由类型:
			v命令 += ca协议字符串[v参数]
		else:
			v命令 += v参数
	if a虚拟路由转发:
		v命令 += a虚拟路由转发
	return v命令
def f取距离(a文本):
	"""必需是"[%d/%d]"格式"""
	v = 字符串.f提取字符串之间(a文本, "[", "]")
	v管理距离s, v度量值s = v.split("/")
	return int(v管理距离s), int(v度量值s)
def f去逗号(a文本):
	if a文本[-1] == ",":
		return a文本[:-1]
	return a文本
#表
class C路由表4:
	c协议开始 = 0
	c网络号开始 = 9
	def __init__(self, a文本):
		self.m文本 = a文本
	def __iter__(self):
		return self.fe条目()
	def fe条目(self):
		def fi条目开头(a行):
			#路由表条目行首字符总是有字符,第9字符总是空格
			return v行[0] != " " and v行[C路由表4.c网络号开始-1] == " "
		def fi主类行(a行):
			#主类行没有能使用的信息
			return v行[6].isdigit()
		def fi说明行(a行):
			#带横杠的是说明
			return "-" in a行
		v详细开始 = -1	#网络号后面开始位置
		for v行 in self.m文本.split("\n"):
			#跳过无关行
			if len(v行) < 40:
				continue	#太短,跳过
			if fi说明行(v行):
				continue
			if fi主类行(v行):
				continue
			#解析
			if fi条目开头(v行):
				v路由类型s = v行[C路由表4.c协议开始 : C路由表4.c网络号开始].strip()
				v详细开始 = v行.find(" ", C路由表4.c网络号开始)
				v网络号s = v行[C路由表4.c网络号开始 : v详细开始]
				v路由类型 = ca代码4[v路由类型s]
				v网络号 = 地址.S网络地址4.fc自动(v网络号s)
			v管理距离 = 0
			v度量值 = 0
			v下一跳 = None
			v出接口 = None
			for v词 in v行[v详细开始+1 : ].split(" "):
				v词 = f去逗号(v词)
				if "[" in v词:	#管理距离&度量值
					v管理距离, v度量值 = f取距离(v词)
				elif v词.count(".") == 3:	#地址
					v下一跳 = 地址.S网络地址4.fc自动(v词)
				elif v词.count(":") == 2:	#存在时间
					pass
				elif 北向接口.c接口正则.fullmatch(v词):
					v出接口 = 实现接口.f创建接口(v词)
				else:	#无关词,跳过
					pass
			yield 北向路由.S路由条目(a网络号 = v网络号, a下一跳 = v下一跳, a出接口 = v出接口, a路由类型 = v路由类型, a优先级 = v管理距离, a度量值 = v度量值)
class C路由表6:
	c协议开始 = 0
	c网络号开始 = 4
	def __init__(self, a文本):
		self.m文本 = a文本
	def __iter__(self):
		return self.fe条目()
	def fe条目(self):
		def fi条目开头(a行):
			#路由表条目行首字符总是有字符,第9字符总是空格
			return v行[0] != " " and v行[C路由表6.c网络号开始-1] == " "
		def fi说明行(a行):
			#带横杠的是说明
			return "-" in a行
		for v行 in self.m文本.split("\n"):
			#跳过无关行
			if len(v行) < 16:
				continue	#太短,跳过
			if fi说明行(v行):
				continue
			#解析
			v下一跳 = None
			v出接口 = None
			if fi条目开头(v行):
				v路由类型s = v行[C路由表6.c协议开始 : C路由表6.c网络号开始].strip()
				v距离开始 = v行.find(" ", C路由表6.c网络号开始)
				v网络号s = v行[C路由表6.c网络号开始 : v距离开始]
				v管理距离, v度量值 = f取距离(v行[v距离开始+1 : ])
				v路由类型 = ca代码6[v路由类型s]
				v网络号 = 地址.S网络地址6.fc自动(v网络号s)
				continue
			for v词 in v行.strip().split(" "):
				v词 = f去逗号(v词)
				if v词.count(":") >= 2:	#地址
					v下一跳 = 地址.S网络地址6.fc自动(v词)
				elif 北向接口.c接口正则.fullmatch(v词):
					v出接口 = 实现接口.f创建接口(v词)
				else:
					pass
			yield 北向路由.S路由条目(a网络号 = v网络号, a下一跳 = v下一跳, a出接口 = v出接口, a路由类型 = v路由类型, a优先级 = v管理距离, a度量值 = v度量值)