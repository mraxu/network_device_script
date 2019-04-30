import enum
#===============================================================================
# 操作
#===============================================================================
class E操作(enum.IntEnum):
	e默认 = 0	#设备默认操作,慎用.大部分情况跟e设置一样
	e设置 = 1	#覆盖原有配置,不存在则创建
	e重置 = 2	#恢复默认配置
	e添加 = 3	#添加多个值
	e删除 = 4	#删除/恢复
	e新建 = 5	#没有则创建,有则报错
	e修改 = 6	#修改配置的部分选项
	e开启 = 10
	e关闭 = 11
def f解析操作(a操作):
	v类型 = type(a操作)
	if v类型 == E操作:
		return a操作
	elif v类型 == bool:
		return E操作.e开启 if a操作 else E操作.e关闭
	elif v类型 == int:
		return E操作.e设置 if a操作 else E操作.e删除
	elif v类型 == str:
		if a操作.isdigit():
			return E操作.e设置 if int(a操作) else E操作.e删除
		elif a操作 in ("no", "undo", "delete", "del"):
			return E操作.e删除
		elif a操作 in ("default", "reset"):
			return E操作.e重置
		elif a操作 in ("add",):
			return E操作.e添加
		elif a操作 in ("set",):
			return E操作.e设置
		elif a操作 in ("enable", "on"):
			return E操作.e开启
		elif a操作 in ("disable", "off"):
			return E操作.e关闭
		elif a操作 == "":
			return E操作.e设置
		else:
			raise ValueError("无法解析的字符串")
	else:
		raise TypeError("无法解析的类型")
ca加操作 = (E操作.e设置, E操作.e新建, E操作.e添加, E操作.e修改, E操作.e开启)
ca减操作 = (E操作.e删除, E操作.e重置, E操作.e关闭)
def fi加操作(a操作):
	"设置,添加,修改都是加操作"
	return a操作 in ca加操作
def fi减操作(a操作):
	return a操作 in ca减操作
def fi开关操作_(a操作, a设置开 = True, a正 = True):
	v反 = not a正
	if a操作 == E操作.e开启:
		return a正
	elif a操作 == E操作.e关闭:
		return v反
	elif a操作 == E操作.e设置:
		return a正 if a设置开 else v反
	elif a操作 == E操作.e删除:
		return v反 if a设置开 else a正
	else:
		raise 异常.X操作(a操作, "指定的操作不是开关")
def fi开操作(a操作, a设置开 = True):
	return fi开关操作_(a操作, a设置开, True)
def fi关操作(a操作, a设置开 = True):
	return fi开关操作_(a操作, a设置开, False)
#===============================================================================
# 自动提交
#===============================================================================
class E自动提交(enum.IntEnum):
	e不提交 = 0
	e退出配置模式时 = 1
	e退出当前模式时 = 2
	e立即 = 3
#===============================================================================
# 方向
#===============================================================================
class E方向(enum.IntEnum):
	e入 = 0
	e出 = 1