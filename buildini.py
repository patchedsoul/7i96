import os
from datetime import datetime

def buildini(parent):
	buildErrors = []
	buildini.result = ''
	configPath = os.path.join(parent.configsDir, parent.configName.text())
	iniFilePath = os.path.join(configPath, parent.configName.text() + '.ini')
	if not os.path.exists(configPath):
		os.mkdir(configPath)

	iniContents = ['# This file was created with the 7i96 Wizard on ']
	iniContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	iniContents.append('# If you make changes to this file your screwed\n')

	# build the [EMC] section
	iniContents.append('\n[EMC]\n')
	iniContents.append('VERSION = {}\n'.format(parent.version.text()))
	iniContents.append('MACHINE = {}\n'.format(parent.configName.text()))
	iniContents.append('DEBUG = {}\n'.format(parent.debugCombo.itemData(parent.debugCombo.currentIndex())))

	# build the [HOSTMOT2] section
	iniContents.append('\n[HOSTMOT2]\n')
	iniContents.append('DRIVER = {}\n'.format('hm2_eth'))
	iniContents.append('IPADDRESS = {}\n'.format(parent.ipCombo.itemData(parent.ipCombo.currentIndex())))
	iniContents.append('BOARD = {}\n'.format(parent.boardCB.itemData(parent.boardCB.currentIndex())))
	iniContents.append('STEPGENS = {}\n'.format(str(parent.stepgensSB.value())))
	iniContents.append('ENCODERS = {}\n'.format(str(parent.encodersSB.value())))
	iniContents.append('SSERIAL_PORT = {}\n'.format(str(parent.sserialSB.value())))

	with open(iniFilePath, 'w') as iniFile:
		iniFile.writelines(iniContents)
	buildini.result = 'Sucess {} file was created'.format(iniFilePath)
	return True
	"""

	# build the [DISPLAY] section
	iniContents.append('\n[DISPLAY]\n')
	iniContents.append('DISPLAY = {}\n'.format(data['DISPLAY']['DISPLAY']))
	iniContents.append('POSITION_OFFSET = {}\n'.format(data['DISPLAY']['POSITION_OFFSET']))
	iniContents.append('POSITION_FEEDBACK = {}\n'.format(data['DISPLAY']['POSITION_FEEDBACK']))
	iniContents.append('CYCLE_TIME = {}\n'.format(data['DISPLAY']['CYCLE_TIME']))
	iniContents.append('INTRO_GRAPHIC = {}\n'.format(data['DISPLAY']['INTRO_GRAPHIC']))
	iniContents.append('INTRO_TIME = {}\n'.format(data['DISPLAY']['INTRO_TIME']))
	iniContents.append('OPEN_FILE = "{}"\n'.format(data['DISPLAY']['OPEN_FILE']))

	# build the [KINS] section
	iniContents.append('\n[KINS]\n')
	iniContents.append('KINEMATICS = {}\n'.format(data['KINS']['KINEMATICS']))
	iniContents.append('JOINTS = {}\n'.format(data['KINS']['JOINTS']))

	# build the [EMCIO] section
	iniContents.append('\n[EMCIO]\n')
	iniContents.append('EMCIO = {}\n'.format(data['EMCIO']['EMCIO']))
	iniContents.append('CYCLE_TIME = {}\n'.format(data['EMCIO']['CYCLE_TIME']))
	iniContents.append('TOOL_TABLE = {}\n'.format(data['EMCIO']['TOOL_TABLE']))

	# build the [RS274NGC] section
	iniContents.append('\n[RS274NGC]\n')
	iniContents.append('PARAMETER_FILE = {}\n'.format(data['RS274NGC']['PARAMETER_FILE']))
	if data['RS274NGC']['RS274NGC_STARTUP_CODE']:
		iniContents.append('RS274NGC_STARTUP_CODE = {}\n'.format(data['RS274NGC']['RS274NGC_STARTUP_CODE']))
	if data['RS274NGC']['SUBROUTINE_PATH']:
		iniContents.append('SUBROUTINE_PATH = {}\n'.format(data['RS274NGC']['SUBROUTINE_PATH']))
	if data['RS274NGC']['USER_M_PATH']:
		iniContents.append('USER_M_PATH = {}\n'.format(data['RS274NGC']['USER_M_PATH']))

	# build the [EMCMOT] section
	iniContents.append('\n[EMCMOT]\n')
	iniContents.append('EMCMOT = {}\n'.format(data['EMCMOT']['EMCMOT']))
	iniContents.append('SERVO_PERIOD = {}\n'.format(data['EMCMOT']['SERVO_PERIOD']))

	# build the [TASK] section
	iniContents.append('\n[TASK]\n')
	iniContents.append('TASK = {}\n'.format(data['TASK']['TASK']))
	iniContents.append('CYCLE_TIME = {}\n'.format(data['TASK']['CYCLE_TIME']))

	# build the [TRAJ] section
	iniContents.append('\n[TRAJ]\n')
	iniContents.append('COORDINATES = {}\n'.format(data['TRAJ']['COORDINATES']))
	iniContents.append('LINEAR_UNITS = {}\n'.format(data['TRAJ']['LINEAR_UNITS']))
	iniContents.append('ANGULAR_UNITS = {}\n'.format(data['TRAJ']['ANGULAR_UNITS']))

	# build the [HAL] section
	iniContents.append('\n[HAL]\n')
	iniContents.append('HALFILE = {}\n'.format(data['HAL']['HALFILE']))
	if data['HAL']['HALUI']:
		iniContents.append('HALUI = {}\n'.format(data['HAL']['HALUI']))
	if data['HAL']['POSTGUI_HALFILE']:
		iniContents.append('POSTGUI_HALFILE = {}\n'.format(data['HAL']['POSTGUI_HALFILE']))
	if data['HAL']['SHUTDOWN']:
		iniContents.append('SHUTDOWN = {}\n'.format(data['HAL']['SHUTDOWN']))

	# build the [HALUI] section
	iniContents.append('\n[HALUI]\n')
	if data['HALUI']['MDI_COMMAND']:
		iniContents.append('MDI_COMMAND = {}\n'.format(data['HALUI']['MDI_COMMAND']))

	# build the [JOINT_0] section
	if data['JOINT_0']['ENABLED']:
		iniContents.append('\n[JOINT_0]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_0']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_0']['SCALE']))

	# build the [JOINT_1] section
	if data['JOINT_1']['ENABLED']:
		iniContents.append('\n[JOINT_1]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_1']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_1']['SCALE']))

	# build the [JOINT_2] section
	if data['JOINT_2']['ENABLED']:
		iniContents.append('\n[JOINT_2]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_2']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_2']['SCALE']))

	# build the [JOINT_3] section
	if data['JOINT_3']['ENABLED']:
		iniContents.append('\n[JOINT_3]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_3']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_3']['SCALE']))

	# build the [JOINT_4] section
	if data['JOINT_4']['ENABLED']:
		iniContents.append('\n[JOINT_4]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_4']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_4']['SCALE']))

	# build the [AXIS_X] section
	if data['AXIS_X']['ENABLED']:
		iniContents.append('\n[AXIS_X]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_X']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_X']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_X']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_X']['MAX_ACCELERATION']))

	# build the [AXIS_Y] section
	if data['AXIS_Y']['ENABLED']:
		iniContents.append('\n[AXIS_Y]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_Y']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_Y']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_Y']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_Y']['MAX_ACCELERATION']))

	# build the [AXIS_Z] section
	if data['AXIS_Z']['ENABLED']:
		iniContents.append('\n[AXIS_Z]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_Z']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_Z']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_Z']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_Z']['MAX_ACCELERATION']))

	# build the [AXIS_A] section
	if data['AXIS_A']['ENABLED']:
		iniContents.append('\n[AXIS_A]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_A']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_A']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_A']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_A']['MAX_ACCELERATION']))

	# build the [AXIS_B] section
	if data['AXIS_B']['ENABLED']:
		iniContents.append('\n[AXIS_B]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_B']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_B']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_B']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_B']['MAX_ACCELERATION']))

	# build the [AXIS_C] section
	if data['AXIS_C']['ENABLED']:
		iniContents.append('\n[AXIS_C]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_C']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_C']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_C']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_C']['MAX_ACCELERATION']))

	# build the [AXIS_U] section

	# build the [AXIS_V] section

	# build the [AXIS_W] section
"""


	#print(iniFileName)
	# for now just write over the file if it exists.
	# fuck the configparser just fucking write the file...
	
	#config = configparser.ConfigParser(strict=False, allow_no_value=True)
	#config.optionxform = str
	#config.sections()
	#config['INFORMATION'] = '# This file was created by the 7i96 Wizard'
	#config['EMC'] = {'MACHINE' : data['EMC']['MACHINE'],
	#								'DEBUG' : '0x00000000'}

	#with open(iniFileName, 'w') as configfile:
	#	config.write(configfile)

	#print(data['EMC']['MACHINE'])
	
	



	"""
	if data['EMC']['MACHINE']: # might just check this before calling buildini
	
	iniContents.append('\n[]\n')
	iniContents.append(' = \n'.format(data['']['']))

"""

def buildHal(data, path, name):
	halFileName = os.path.join(path, name + '.hal')
	halContents = []
	halContents.append('# kinematics\n')
	halContents.append('loadrt [KINS]KINEMATICS\n')
	halContents.append('\n')
	halContents.append('# motion controller\n')
	halContents.append('loadrt [EMCMOT]EMCMOT ')
	halContents.append('servo_period_nsec=[EMCMOT]SERVO_PERIOD ')
	halContents.append('num_joints=[KINS]JOINTS\n')
	halContents.append('\n')
	halContents.append('# standard components\n')
	# this needs to be calculated by how many axies are enabled
	halContents.append('loadrt pid num_chan=4 \n')
	halContents.append('\n')
	halContents.append('# hostmot2 driver\n')
	halContents.append('loadrt hostmot2\n')
	halContents.append('\n')
	halContents.append('# load low-level driver\n')
	halContents.append('loadrt [HOSTMOT2](DRIVER) ')
	halContents.append('board_ip=[HOSTMOT2](IP) ')
	halContents.append('config=[HOSTMOT2](CONFIG)\n')
	halContents.append('\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.watchdog.timeout_ns 25000000\n')
	halContents.append('\n')
	halContents.append('# THREADS\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.read servo-thread\n')
	halContents.append('addf motion-command-handler servo-thread\n')
	halContents.append('addf motion-controller servo-thread\n')
	halContents.append('addf pid.0.do-pid-calcs servo-thread\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.write servo-thread\n')

	with open(halFileName, 'w') as iniFile:
		iniFile.writelines(halContents)

	buildHal.result = ''	
	return True
