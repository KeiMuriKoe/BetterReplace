from operator import iconcat
from platform import release
from statistics import variance
from textwrap import wrap
import tkinter as tk
import clipboard
from tkinter import ttk

def copy_result():
	a = text_result.get('1.0', 'end')
	clipboard.copy(a)



def detect_from():
		global detected_from
		detected_from = int
		detected_from = rad_from.get()
		if detected_from == 1:
			value_in_wood_option_from.set('Enter wood type')
			optionmenu_wood_from['menu'].delete(0, 'end')
			new_mine_from_choices = ('acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'oak', 'spruce', 'warped')
			for choice in new_mine_from_choices:
				optionmenu_wood_from['menu'].add_command(label=choice,
														 command=tk._setit(value_in_wood_option_from, choice))
		elif detected_from == 2:
			value_in_wood_option_from.set('Enter wood type')
			optionmenu_wood_from['menu'].delete(0, 'end')
			new_mine_from_choices = ('acacia', 'ash', 'aspen', 'birch', 'blackwood', 'chestnut', 'douglas_fir', 'hickory', 'kapok', 'maple', 'oak', 'palm', 'pine', 'rosewood', 'sequoia', 'spruce', 'sycamore', 'white_cedar', 'willow')
			for choice in new_mine_from_choices:
				optionmenu_wood_from['menu'].add_command(label=choice,
														 command=tk._setit(value_in_wood_option_from, choice))


def detect_to():
	global detected_to
	detected_to = int
	detected_to = rad_to.get()
	if detected_to == 1:
		value_in_wood_option_to.set('Enter wood type')
		optionmenu_wood_to['menu'].delete(0, 'end')
		new_mine_to_choices = ('acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'oak', 'spruce', 'warped')
		for choice in new_mine_to_choices:
			optionmenu_wood_to['menu'].add_command(label=choice,
													 command=tk._setit(value_in_wood_option_to, choice))
	elif detected_to == 2:
		value_in_wood_option_to.set('Enter wood type')
		optionmenu_wood_to['menu'].delete(0, 'end')
		new_mine_to_choices = (
		'acacia', 'ash', 'aspen', 'birch', 'blackwood', 'chestnut', 'douglas_fir', 'hickory', 'kapok', 'maple', 'oak',
		'palm', 'pine', 'rosewood', 'sequoia', 'spruce', 'sycamore', 'white_cedar', 'willow')
		for choice in new_mine_to_choices:
			optionmenu_wood_to['menu'].add_command(label=choice,
													 command=tk._setit(value_in_wood_option_to, choice))



def print_result() :
	text_result.delete('1.0', 'end')
	result_str = str
	xyz = str
	xyz = Entry_xyz.get()
	xyz = xyz.strip()
	fill_value = "{id:command_block_minecart,Command:'"+'fill '+ xyz + ' '


# planks
	if detected_from == 1:
		planks1_pre = 'minecraft:'
		planks1_post = '_planks'
	elif detected_from == 2:
		planks1_pre = str
		planks1_pre = 'tfc:wood/planks/'
		planks1_post = str
		planks1_post = ''
	planks1 = str
	planks1 = value_in_wood_option_from.get()
	planks1 = planks1_pre + planks1 + planks1_post

	if detected_to == 1:
		planks2_pre = 'minecraft:'
		planks2_post = '_planks'
	elif detected_to == 2:
		planks2_pre = 'tfc:wood/planks/'
		planks2_post = ''
	planks2 = str
	planks2 = value_in_wood_option_to.get()
	planks2 = planks2_pre + planks2 + planks2_post
	Planks_res = fill_value + planks2 + ' replace ' + planks1 + "'},"

# wood
	wood1 = str
	wood1 = value_in_wood_option_from.get()
	if wood1 == 'crimson':
		wood1_post = str
		wood1_post = '_hyphae'
	elif wood1 == 'warped':
		wood1_post = str
		wood1_post = '_hyphae'
	else:
		wood1_post = str
		wood1_post = '_wood'

	if detected_from == 1:
		wood1_pre = 'minecraft:'
	elif detected_from == 2:
		wood1_pre = 'tfc:wood/wood/'
		wood1_post = ''

	wood1 = wood1_pre + wood1 + wood1_post

	wood2 = str
	wood2 = value_in_wood_option_to.get()
	if wood2 == 'crimson':
		wood2_post = str
		wood2_post = '_hyphae'
	elif wood2 == 'warped':
		wood2_post = str
		wood2_post = '_hyphae'
	else:
		wood2_post = str
		wood2_post = '_wood'

	if detected_to == 1:
		wood2_pre = 'minecraft:'
	elif detected_to == 2:
		wood2_pre = 'tfc:wood/wood/'
		wood2_post = ''

	wood2 = wood2_pre + wood2 + wood2_post
	Wood_res = fill_value + wood2 + ' replace ' + wood1 + "'},"

# stripped wood
	strwood1 = str
	strwood1 = value_in_wood_option_from.get()
	if strwood1 == 'crimson':
		strwood1_post = str
		strwood1_post = '_hyphae'
	elif strwood1 == 'warped':
		strwood1_post = str
		strwood1_post = '_hyphae'
	else:
		strwood1_post = str
		strwood1_post = '_wood'

	if detected_from == 1:
		strwood1_pre = 'minecraft:stripped_'
	elif detected_from == 2:
		strwood1_pre = 'tfc:wood/stripped_wood/'
		strwood1_post = ''

	strwood1 = strwood1_pre + strwood1 + strwood1_post

	strwood2 = str
	strwood2 = value_in_wood_option_to.get()
	if strwood2 == 'crimson':
		strwood2_post = str
		strwood2_post = '_hyphae'
	elif strwood2 == 'warped':
		strwood2_post = str
		strwood2_post = '_hyphae'
	else:
		strwood2_post = str
		strwood2_post = '_wood'

	if detected_to == 1:
		strwood2_pre = 'minecraft:stripped_'
	elif detected_to == 2:
		strwood2_pre = 'tfc:wood/stripped_wood/'
		strwood2_post = ''


	strwood2 = strwood2_pre + strwood2 + strwood2_post
	strWood_res = fill_value + strwood2 + ' replace ' + strwood1 + "'},"

#bookshelf
	if detected_from == 1:
		bookshelf1_pre = 'minecraft:bookshelf'
		bookshelf1_post = ''
	elif detected_from == 2:
		bookshelf1_pre = str
		bookshelf1_pre = 'tfc:wood/planks/'
		bookshelf1_post = str
		bookshelf1_post = '_bookshelf'
	bookshelf1 = str
	bookshelf1 = ''
	if detected_from == 2:
		bookshelf1 = value_in_wood_option_from.get()
	bookshelf1 = bookshelf1_pre + bookshelf1 + bookshelf1_post

	if detected_to == 1:
		bookshelf2_pre = 'minecraft:bookshelf'
		bookshelf2_post = ''
	elif detected_to == 2:
		bookshelf2_pre = 'tfc:wood/planks/'
		bookshelf2_post = '_bookshelf'
	bookshelf2 = str
	bookshelf2 = ''
	if detected_to ==2:
		bookshelf2 = value_in_wood_option_to.get()
	bookshelf2 = bookshelf2_pre + bookshelf2 + bookshelf2_post
	bookshelf_res = fill_value + bookshelf2 + ' replace ' + bookshelf1 + "'},"

#crafting_table / workbench
	if detected_from == 1:
		workbench1_pre = 'minecraft:crafting_table'
		workbench1_post = ''
	elif detected_from == 2:
		workbench1_pre = str
		workbench1_pre = 'tfc:wood/planks/'
		workbench1_post = str
		workbench1_post = '_workbench'
	workbench1 = str
	workbench1 = ''
	if detected_from == 2:
		workbench1 = value_in_wood_option_from.get()
	workbench1 = workbench1_pre + workbench1 + workbench1_post

	if detected_to == 1:
		workbench2_pre = 'minecraft:crafting_table'
		workbench2_post = ''
	elif detected_to == 2:
		workbench2_pre = 'tfc:wood/planks/'
		workbench2_post = '_workbench'
	workbench2 = str
	workbench2 = ''
	if detected_to ==2:
		workbench2 = value_in_wood_option_to.get()
	workbench2 = workbench2_pre + workbench2 + workbench2_post
	workbench_res = fill_value + workbench2 + ' replace ' + workbench1 + "'},"

#fence
	if detected_from == 1:
		fence1_pre = 'minecraft:'
		fence1_post = '_fence'
	elif detected_from == 2:
		fence1_pre = str
		fence1_pre = 'tfc:wood/planks/'
		fence1_post = str
		fence1_post = '_fence'
	fence1 = str
	fence1 = value_in_wood_option_from.get()
	fence1 = fence1_pre + fence1 + fence1_post

	if detected_to == 1:
		fence2_pre = 'minecraft:'
		fence2_post = '_fence'
	elif detected_to == 2:
		fence2_pre = 'tfc:wood/planks/'
		fence2_post = '_fence'
	fence2 = str
	fence2 = value_in_wood_option_to.get()
	fence2 = fence2_pre + fence2 + fence2_post
	fence_res = fill_value + fence2 + ' replace ' + fence1 + "'},"

# fence_gate
	if detected_from == 1:
		fence_gate1_pre = 'minecraft:'
		fence_gate1_post = '_fence_gate'
	elif detected_from == 2:
		fence_gate1_pre = str
		fence_gate1_pre = 'tfc:wood/planks/'
		fence_gate1_post = str
		fence_gate1_post = '_fence_gate'
	fence_gate1 = str
	fence_gate1 = value_in_wood_option_from.get()
	fence_gate1 = fence_gate1_pre + fence_gate1 + fence_gate1_post

	if detected_to == 1:
		fence_gate2_pre = 'minecraft:'
		fence_gate2_post = '_fence_gate'
	elif detected_to == 2:
		fence_gate2_pre = 'tfc:wood/planks/'
		fence_gate2_post = '_fence_gate'
	fence_gate2 = str
	fence_gate2 = value_in_wood_option_to.get()
	fence_gate2 = fence_gate2_pre + fence_gate2 + fence_gate2_post
	fence_gate_north_res = fill_value + fence_gate2 + '[facing=north]' + ' replace ' + fence_gate1 + '[facing=north]' + "'},"
	fence_gate_east_res = fill_value + fence_gate2 + '[facing=east]' + ' replace ' + fence_gate1 + '[facing=east]' + "'},"
	fence_gate_south_res = fill_value + fence_gate2 + '[facing=south]' + ' replace ' + fence_gate1 + '[facing=south]' + "'},"
	fence_gate_west_res = fill_value + fence_gate2 +  '[facing=west]' +' replace ' + fence_gate1 + '[facing=west]' + "'},"

#button
	if detected_from == 1:
		button1_pre = 'minecraft:'
		button1_post = '_button'
	elif detected_from == 2:
		button1_pre = str
		button1_pre = 'tfc:wood/planks/'
		button1_post = str
		button1_post = '_button'
	button1 = str
	button1 = value_in_wood_option_from.get()
	button1 = button1_pre + button1 + button1_post

	if detected_to == 1:
		button2_pre = 'minecraft:'
		button2_post = '_button'
	elif detected_to == 2:
		button2_pre = 'tfc:wood/planks/'
		button2_post = '_button'
	button2 = str
	button2 = value_in_wood_option_to.get()
	button2 = button2_pre + button2 + button2_post
	button_wall_north_res = fill_value + button2 + '[face=wall,facing=north]' + ' replace ' + button1 + '[face=wall,facing=north]' + "'},"
	button_wall_east_res = fill_value + button2 + '[face=wall,facing=east]' + ' replace ' + button1 + '[face=wall,facing=east]' + "'},"
	button_wall_south_res = fill_value + button2 + '[face=wall,facing=south]' + ' replace ' + button1 + '[face=wall,facing=south]' + "'},"
	button_wall_west_res = fill_value + button2 +  '[face=wall,facing=west]' +' replace ' + button1 + '[face=wall,facing=west]' + "'},"
	button_floor_res = fill_value + button2 + '[face=floor]' + ' replace ' + button1 + '[face=floor]' + "'},"
	button_ceiling_res = fill_value + button2 + '[face=ceiling]' + ' replace ' + button1 + '[face=ceiling]' + "'},"

#pressure_plate
	if detected_from == 1:
		press_plate1_pre = 'minecraft:'
		press_plate1_post = '_pressure_plate'
	elif detected_from == 2:
		press_plate1_pre = str
		press_plate1_pre = 'tfc:wood/planks/'
		press_plate1_post = str
		press_plate1_post = '_pressure_plate'
	press_plate1 = str
	press_plate1 = value_in_wood_option_from.get()
	press_plate1 = press_plate1_pre + press_plate1 + press_plate1_post

	if detected_to == 1:
		press_plate2_pre = 'minecraft:'
		press_plate2_post = '_pressure_plate'
	elif detected_to == 2:
		press_plate2_pre = 'tfc:wood/planks/'
		press_plate2_post = '_pressure_plate'
	press_plate2 = str
	press_plate2 = value_in_wood_option_to.get()
	press_plate2 = press_plate2_pre + press_plate2 + press_plate2_post
	press_plate_res = fill_value + press_plate2 + ' replace ' + press_plate1 + "'},"

#log
	log1 = str
	log1 = value_in_wood_option_from.get()
	if log1 == 'crimson':
		log1_post = str
		log1_post = '_stem'
	elif log1 == 'warped':
		log1_post = str
		log1_post = '_stem'
	else:
		log1_post = str
		log1_post = '_log'

	if detected_from == 1:
		log1_pre = 'minecraft:'
	elif detected_from == 2:
		log1_pre = 'tfc:wood/log/'
		log1_post = ''

	log1 = log1_pre + log1 + log1_post

	log2 = str
	log2 = value_in_wood_option_to.get()
	if log2 == 'crimson':
		log2_post = str
		log2_post = '_stem'
	elif log2 == 'warped':
		log2_post = str
		log2_post = '_stem'
	else:
		log2_post = str
		log2_post = '_log'

	if detected_to == 1:
		log2_pre = 'minecraft:'
	elif detected_to == 2:
		log2_pre = 'tfc:wood/log/'
		log2_post = ''

	log2 = log2_pre + log2 + log2_post

	log_x_res = fill_value + log2 + '[axis=x]' + ' replace ' + log1 + '[axis=x]' + "'},"
	log_y_res = fill_value + log2 + '[axis=y]' + ' replace ' + log1 + '[axis=y]' + "'},"
	log_z_res = fill_value + log2 + '[axis=z]' + ' replace ' + log1 + '[axis=z]' + "'},"

# stripped log
	strlog1 = str
	strlog1 = value_in_wood_option_from.get()
	if strlog1 == 'crimson':
		strlog1_post = str
		strlog1_post = '_stem'
	elif strlog1 == 'warped':
		strlog1_post = str
		strlog1_post = '_stem'
	else:
		strlog1_post = str
		strlog1_post = '_log'

	if detected_from == 1:
		strlog1_pre = 'minecraft:stripped_'
	elif detected_from == 2:
		strlog1_pre = 'tfc:wood/stripped_log/'
		strlog1_post = ''

	strlog1 = strlog1_pre + strlog1 + strlog1_post

	strlog2 = str
	strlog2 = value_in_wood_option_to.get()
	if strlog2 == 'crimson':
		strlog2_post = str
		strlog2_post = '_stem'
	elif strlog2 == 'warped':
		strlog2_post = str
		strlog2_post = '_stem'
	else:
		strlog2_post = str
		strlog2_post = '_log'

	if detected_to == 1:
		strlog2_pre = 'minecraft:stripped_'
	elif detected_to == 2:
		strlog2_pre = 'tfc:wood/stripped_log/'
		strlog2_post = ''

	strlog2 = strlog2_pre + strlog2 + strlog2_post

	strlog_x_res = fill_value + strlog2 + '[axis=x]' + ' replace ' + strlog1 + '[axis=x]' + "'},"
	strlog_y_res = fill_value + strlog2 + '[axis=y]' + ' replace ' + strlog1 + '[axis=y]' + "'},"
	strlog_z_res = fill_value + strlog2 + '[axis=z]' + ' replace ' + strlog1 + '[axis=z]' + "'},"

#slab
	if detected_from == 1:
		slab1_pre = 'minecraft:'
		slab1_post = '_slab'
	elif detected_from == 2:
		slab1_pre = str
		slab1_pre = 'tfc:wood/planks/'
		slab1_post = str
		slab1_post = '_slab'
	slab1 = str
	slab1 = value_in_wood_option_from.get()
	slab1 = slab1_pre + slab1 + slab1_post

	if detected_to == 1:
		slab2_pre = 'minecraft:'
		slab2_post = '_slab'
	elif detected_to == 2:
		slab2_pre = 'tfc:wood/planks/'
		slab2_post = '_slab'
	slab2 = str
	slab2 = value_in_wood_option_to.get()
	slab2 = slab2_pre + slab2 + slab2_post
	slab_bottom_res = fill_value +  slab2 + '[type=bottom]' + ' replace ' + slab1 + '[type=bottom]' + "'},"
	slab_double_res = fill_value + slab2 + '[type=double]' + ' replace ' + slab1 + '[type=double]' + "'},"
	slab_top_res = fill_value + slab2 + '[type=top]' + ' replace ' + slab1 + '[type=top]' + "'},"

#stairs
	if detected_from == 1:
		stairs1_pre = 'minecraft:'
		stairs1_post = '_stairs'
	elif detected_from == 2:
		stairs1_pre = str
		stairs1_pre = 'tfc:wood/planks/'
		stairs1_post = str
		stairs1_post = '_stairs'
	stairs1 = str
	stairs1 = value_in_wood_option_from.get()
	stairs1 = stairs1_pre + stairs1 + stairs1_post

	if detected_to == 1:
		stairs2_pre = 'minecraft:'
		stairs2_post = '_stairs'
	elif detected_to == 2:
		stairs2_pre = 'tfc:wood/planks/'
		stairs2_post = '_stairs'
	stairs2 = str
	stairs2 = value_in_wood_option_to.get()
	stairs2 = stairs2_pre + stairs2 + stairs2_post
	stairs_north_bottom_res = fill_value +  stairs2 + '[facing=north,' + 'half=bottom]' + ' replace ' + stairs1 + '[facing=north,' + 'half=bottom]' + "'},"
	stairs_south_bottom_res = fill_value + stairs2 + '[facing=south,' + 'half=bottom]' + ' replace ' + stairs1 + '[facing=south,' + 'half=bottom]' + "'},"
	stairs_west_bottom_res = fill_value + stairs2 + '[facing=west,' + 'half=bottom]' + ' replace ' + stairs1 + '[facing=west,' + 'half=bottom]' + "'},"
	stairs_east_bottom_res = fill_value + stairs2 + '[facing=east,' + 'half=bottom]' + ' replace ' + stairs1 + '[facing=east,' + 'half=bottom]' + "'},"
	stairs_north_top_res = fill_value +  stairs2 + '[facing=north,' + 'half=top]' + ' replace ' + stairs1 + '[facing=north,' + 'half=top]' + "'},"
	stairs_south_top_res = fill_value + stairs2 + '[facing=south,' + 'half=top]' + ' replace ' + stairs1 + '[facing=south,' + 'half=top]' + "'},"
	stairs_west_top_res = fill_value + stairs2 + '[facing=west,' + 'half=top]' + ' replace ' + stairs1 + '[facing=west,' + 'half=top]' + "'},"
	stairs_east_top_res = fill_value + stairs2 + '[facing=east,' + 'half=top]' + ' replace ' + stairs1 + '[facing=east,' + 'half=top]' + "'},"

#trapdoor
	if detected_from == 1:
		trapdoor1_pre = 'minecraft:'
		trapdoor1_post = '_trapdoor'
	elif detected_from == 2:
		trapdoor1_pre = str
		trapdoor1_pre = 'tfc:wood/planks/'
		trapdoor1_post = str
		trapdoor1_post = '_trapdoor'
	trapdoor1 = str
	trapdoor1 = value_in_wood_option_from.get()
	trapdoor1 = trapdoor1_pre + trapdoor1 + trapdoor1_post

	if detected_to == 1:
		trapdoor2_pre = 'minecraft:'
		trapdoor2_post = '_trapdoor'
	elif detected_to == 2:
		trapdoor2_pre = 'tfc:wood/planks/'
		trapdoor2_post = '_trapdoor'
	trapdoor2 = str
	trapdoor2 = value_in_wood_option_to.get()
	trapdoor2 = trapdoor2_pre + trapdoor2 + trapdoor2_post
	trapdoor_north_bottom_open_res = fill_value +  trapdoor2 + '[facing=north,' + 'half=bottom,open=true]' + ' replace ' + trapdoor1 + '[facing=north,' + 'half=bottom,open=true]' + "'},"
	trapdoor_south_bottom_open_res = fill_value + trapdoor2 + '[facing=south,' + 'half=bottom,open=true]' + ' replace ' + trapdoor1 + '[facing=south,' + 'half=bottom,open=true]' + "'},"
	trapdoor_west_bottom_open_res = fill_value + trapdoor2 + '[facing=west,' + 'half=bottom,open=true]' + ' replace ' + trapdoor1 + '[facing=west,' + 'half=bottom,open=true]' + "'},"
	trapdoor_east_bottom_open_res = fill_value + trapdoor2 + '[facing=east,' + 'half=bottom,open=true]' + ' replace ' + trapdoor1 + '[facing=east,' + 'half=bottom,open=true]' + "'},"
	trapdoor_north_top_open_res = fill_value +  trapdoor2 + '[facing=north,' + 'half=top,open=true]' + ' replace ' + trapdoor1 + '[facing=north,' + 'half=top,open=true]' + "'},"
	trapdoor_south_top_open_res = fill_value + trapdoor2 + '[facing=south,' + 'half=top,open=true]' + ' replace ' + trapdoor1 + '[facing=south,' + 'half=top,open=true]' + "'},"
	trapdoor_west_top_open_res = fill_value + trapdoor2 + '[facing=west,' + 'half=top,open=true]' + ' replace ' + trapdoor1 + '[facing=west,' + 'half=top,open=true]' + "'},"
	trapdoor_east_top_open_res = fill_value + trapdoor2 + '[facing=east,' + 'half=top,open=true]' + ' replace ' + trapdoor1 + '[facing=east,' + 'half=top,open=true]' + "'},"
	trapdoor_north_bottom_closed_res = fill_value +  trapdoor2 + '[facing=north,' + 'half=bottom,open=false]' + ' replace ' + trapdoor1 + '[facing=north,' + 'half=bottom,open=false]' + "'},"
	trapdoor_south_bottom_closed_res = fill_value + trapdoor2 + '[facing=south,' + 'half=bottom,open=false]' + ' replace ' + trapdoor1 + '[facing=south,' + 'half=bottom,open=false]' + "'},"
	trapdoor_west_bottom_closed_res = fill_value + trapdoor2 + '[facing=west,' + 'half=bottom,open=false]' + ' replace ' + trapdoor1 + '[facing=west,' + 'half=bottom,open=false]' + "'},"
	trapdoor_east_bottom_closed_res = fill_value + trapdoor2 + '[facing=east,' + 'half=bottom,open=false]' + ' replace ' + trapdoor1 + '[facing=east,' + 'half=bottom,open=false]' + "'},"
	trapdoor_north_top_closed_res = fill_value +  trapdoor2 + '[facing=north,' + 'half=top,open=false]' + ' replace ' + trapdoor1 + '[facing=north,' + 'half=top,open=false]' + "'},"
	trapdoor_south_top_closed_res = fill_value + trapdoor2 + '[facing=south,' + 'half=top,open=false]' + ' replace ' + trapdoor1 + '[facing=south,' + 'half=top,open=false]' + "'},"
	trapdoor_west_top_closed_res = fill_value + trapdoor2 + '[facing=west,' + 'half=top,open=false]' + ' replace ' + trapdoor1 + '[facing=west,' + 'half=top,open=false]' + "'},"
	trapdoor_east_top_closed_res = fill_value + trapdoor2 + '[facing=east,' + 'half=top,open=false]' + ' replace ' + trapdoor1 + '[facing=east,' + 'half=top,open=false]' + "'},"

#chest
	if detected_from == 1:
		chest1_pre = 'minecraft:chest'
		chest1_post = ''
	elif detected_from == 2:
		chest1_pre = str
		chest1_pre = 'tfc:wood/chest/'
		chest1_post = str
		chest1_post = ''
	chest1 = str
	chest1 = ''
	if detected_from == 2:
		chest1 = value_in_wood_option_from.get()
	chest1 = chest1_pre + chest1 + chest1_post

	if detected_to == 1:
		chest2_pre = 'minecraft:chest'
		chest2_post = ''
	elif detected_to == 2:
		chest2_pre = str
		chest2_pre = 'tfc:wood/chest/'
		chest2_post = str
		chest2_post = ''
	chest2 = str
	chest2 = ''
	if detected_to == 2:
		chest2 = value_in_wood_option_to.get()
	chest2 = chest2_pre + chest2 + chest2_post

	chest_north_res = fill_value + chest2 + '[facing=north]' + ' replace ' + chest1 + '[facing=north]' + "'},"
	chest_east_res = fill_value + chest2 + '[facing=east]' + ' replace ' + chest1 + '[facing=east]' + "'},"
	chest_south_res = fill_value + chest2 + '[facing=south]' + ' replace ' + chest1 + '[facing=south]' + "'},"
	chest_west_res = fill_value + chest2 +  '[facing=west]' +' replace ' + chest1 + '[facing=west]' + "'},"

# barrel
	if detected_from == 1:
		barrel1_pre = 'minecraft:barrel'
		barrel1_post = ''
	elif detected_from == 2:
		barrel1_pre = str
		barrel1_pre = 'tfc:wood/barrel/'
		barrel1_post = str
		barrel1_post = ''
	barrel1 = str
	barrel1 = ''
	if detected_from == 2:
		barrel1 = value_in_wood_option_from.get()
	barrel1 = barrel1_pre + barrel1 + barrel1_post

	if detected_to == 1:
		barrel2_pre = 'minecraft:barrel'
		barrel2_post = ''
	elif detected_to == 2:
		barrel2_pre = str
		barrel2_pre = 'tfc:wood/barrel/'
		barrel2_post = str
		barrel2_post = ''
	barrel2 = str
	barrel2 = ''
	if detected_to == 2:
		barrel2 = value_in_wood_option_to.get()
	barrel2 = barrel2_pre + barrel2 + barrel2_post

	barrel_res = fill_value + barrel2 + ' replace ' + barrel1 + "'},"

# trapped chest
	if detected_from == 1:
		trap_chest1_pre = 'minecraft:trapped_chest'
		trap_chest1_post = ''
	elif detected_from == 2:
		trap_chest1_pre = str
		trap_chest1_pre = 'tfc:wood/trapped_chest/'
		trap_chest1_post = str
		trap_chest1_post = ''
	trap_chest1 = str
	trap_chest1 = ''
	if detected_from == 2:
		trap_chest1 = value_in_wood_option_from.get()
	trap_chest1 = trap_chest1_pre + trap_chest1 + trap_chest1_post

	if detected_to == 1:
		trap_chest2_pre = 'minecraft:trapped_chest'
		trap_chest2_post = ''
	elif detected_to == 2:
		trap_chest2_pre = str
		trap_chest2_pre = 'tfc:wood/trapped_chest/'
		trap_chest2_post = str
		trap_chest2_post = ''
	trap_chest2 = str
	trap_chest2 = ''
	if detected_to == 2:
		trap_chest2 = value_in_wood_option_to.get()
	trap_chest2 = trap_chest2_pre + trap_chest2 + trap_chest2_post

	trap_chest_north_res = fill_value + trap_chest2 + '[facing=north]' + ' replace ' + trap_chest1 + '[facing=north]' + "'},"
	trap_chest_east_res = fill_value + trap_chest2 + '[facing=east]' + ' replace ' + trap_chest1 + '[facing=east]' + "'},"
	trap_chest_south_res = fill_value + trap_chest2 + '[facing=south]' + ' replace ' + trap_chest1 + '[facing=south]' + "'},"
	trap_chest_west_res = fill_value + trap_chest2 + '[facing=west]' + ' replace ' + trap_chest1 + '[facing=west]' + "'},"

# torch
	if detected_from == 1:
		torch1_pre = 'minecraft:'
		torch1_mid = 'wall_'
		torch1_post = 'torch'
	elif detected_from == 2:
		torch1_pre = 'tfc:'
		torch1_mid = 'wall_'
		torch1_post = 'torch'
	torch1 = str
	torch_wall_1 = str
	torch1 = torch1_pre + torch1_post
	torch_wall_1 = torch1_pre + torch1_mid +torch1_post

	if detected_to == 1:
		torch2_pre = 'minecraft:'
		torch2_mid = 'wall_'
		torch2_post = 'torch'
	elif detected_to == 2:
		torch2_pre = 'tfc:'
		torch2_mid = 'wall_'
		torch2_post = 'torch'
	torch2 = str
	torch_wall_2 = str
	torch2 = torch2_pre + torch2_post
	torch_wall_2 = torch2_pre + torch2_mid + torch2_post

	torch_res = fill_value + torch2 + ' replace ' + torch1 + "'},"

	if detected_from == 2 and detected_to == 1:
		dead_wall_torch_north_res = fill_value + 'minecraft:wall_torch[facing=north] replace ' + 'tfc:dead_wall_torch[facing=north]' + "'},"
		dead_wall_torch_east_res = fill_value + 'minecraft:wall_torch[facing=east] replace ' + 'tfc:dead_wall_torch[facing=east]' + "'},"
		dead_wall_torch_south_res = fill_value + 'minecraft:wall_torch[facing=south] replace ' + 'tfc:dead_wall_torch[facing=south]' + "'},"
		dead_wall_torch_west_res = fill_value + 'minecraft:wall_torch[facing=west] replace ' + 'tfc:dead_wall_torch[facing=west]' + "'},"
		dead_torch_res = fill_value + 'minecraft:torch replace ' + 'tfc:dead_torch' + "'},"
	else:
		dead_wall_torch_north_res = ''
		dead_wall_torch_east_res = ''
		dead_wall_torch_south_res = ''
		dead_wall_torch_west_res = ''
		dead_torch_res = ''

	torch_wall_north_res = fill_value + torch_wall_2 + '[facing=north]' + ' replace ' + torch_wall_1 + '[facing=north]' + "'},"
	torch_wall_east_res = fill_value + torch_wall_2 + '[facing=east]' + ' replace ' + torch_wall_1 + '[facing=east]' + "'},"
	torch_wall_south_res = fill_value + torch_wall_2 + '[facing=south]' + ' replace ' + torch_wall_1 + '[facing=south]' + "'},"
	torch_wall_west_res = fill_value + torch_wall_2 + '[facing=west]' + ' replace ' + torch_wall_1 + '[facing=west]' + "'},"

	result_str = "summon falling_block ~ ~1 ~ {BlockState:{Name:redstone_block},Passengers:[" \
				 "{id:armor_stand,Health:0,Passengers:[" \
				 "{id:falling_block,BlockState:{Name:activator_rail},Passengers:[" \
				 "{id:command_block_minecart,Command:'gamerule commandBlockOutput false'}," \
				 "{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},"\
				 + Planks_res + Wood_res + strWood_res + bookshelf_res + workbench_res + fence_res + fence_gate_north_res + fence_gate_east_res + \
				 fence_gate_south_res + fence_gate_west_res + press_plate_res + button_wall_north_res + button_wall_east_res + button_wall_south_res + button_wall_west_res + button_floor_res + \
				 button_ceiling_res + log_x_res + log_y_res + log_z_res + strlog_x_res + strlog_y_res + strlog_z_res + slab_bottom_res + slab_double_res + slab_top_res + stairs_north_bottom_res +\
				 stairs_south_bottom_res + stairs_west_bottom_res + stairs_east_bottom_res + stairs_north_top_res + stairs_south_top_res + stairs_west_top_res + stairs_east_top_res + trapdoor_north_bottom_open_res \
				 + trapdoor_south_bottom_open_res + trapdoor_west_bottom_open_res + trapdoor_east_bottom_open_res + trapdoor_north_top_open_res + trapdoor_south_top_open_res + trapdoor_west_top_open_res + trapdoor_east_top_open_res + trapdoor_north_bottom_closed_res + \
				 trapdoor_south_bottom_closed_res + trapdoor_west_bottom_closed_res + trapdoor_east_bottom_closed_res + trapdoor_north_top_closed_res + trapdoor_south_top_closed_res + trapdoor_west_top_closed_res + trapdoor_east_top_closed_res + chest_north_res + chest_east_res + chest_south_res + \
				 chest_west_res + barrel_res + trap_chest_north_res + trap_chest_east_res + trap_chest_south_res + trap_chest_west_res + torch_res + torch_wall_north_res + torch_wall_east_res + torch_wall_south_res + torch_wall_west_res + dead_wall_torch_north_res + dead_wall_torch_east_res + dead_wall_torch_south_res + dead_wall_torch_west_res + dead_torch_res +\
				 "{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:" + '"fill ~ ~ ~ ~ ~-3 ~ air"' +\
				 "}'},{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}"

	text_result.insert( 0.0, result_str)



win = tk.Tk()
# win.iconbitmap('minecraft.256x256.ico')
win.title('BetterReplace')
win.geometry('400x425+760+240')
win.resizable(False,False)
win.config(bg='#454545')

label_xyz = tk.Label(win, text='Enter xyz:',bg='#454545', fg='#ffffff',font=('Arial',13,'bold')).grid(row=0,column=0)

Entry_xyz = tk.Entry(win,bg='#262626',fg='#ffffff',selectbackground='lightblue',selectforeground='#454545',bd=0)
Entry_xyz.grid(row=0, column=1,pady=25)


label_from=tk.Label(win, text='Replace blocks from :',bg='#454545', fg='#ffffff',font=('Arial',10,'bold')).grid(row=1,column=0)
label_to=tk.Label(win, text='Replace blocks to :',bg='#454545', fg='#ffffff',font=('Arial',10,'bold')).grid(row=1,column=1)

rad_from=tk.IntVar()
rad_to=tk.IntVar()


def on_rad_mine_from(e):
    rad_mine_from['foreground'] = '#262626'

def on_rad_mine_from_leave(e):
    rad_mine_from['foreground'] = '#ffffff'

def on_rad_tfc_from(e):
	rad_tfc_from['foreground'] = '#262626'

def on_rad_tfc_from_leave(e):
	rad_tfc_from['foreground'] = '#ffffff'

def on_rad_mine_to(e):
    rad_mine_to['foreground'] = '#262626'

def on_rad_mine_to_leave(e):
    rad_mine_to['foreground'] = '#ffffff'

def on_rad_tfc_to(e):
	rad_tfc_to['foreground'] = '#262626'

def on_rad_tfc_to_leave(e):
	rad_tfc_to['foreground'] = '#ffffff'

rad_mine_from = tk.Radiobutton(win, text='Minecraft', variable=rad_from, value=1, command = detect_from, fg='#dddddd',selectcolor='#535353', bg='#454545',activebackground='#454545',activeforeground='#262626')
rad_mine_from.grid(row=2,column=0,pady=2)
rad_tfc_from = tk.Radiobutton(win, text='TerraFirmaCraft', variable=rad_from, value=2,command = detect_from, fg='#dddddd',selectcolor='#535353', bg='#454545',activebackground='#454545',activeforeground='#262626')
rad_tfc_from.grid(row=3,column=0,pady=2)

rad_mine_to = tk.Radiobutton(win, text='Minecraft', variable=rad_to, value=1,fg='#dddddd',command = detect_to, selectcolor='#535353', bg='#454545',activebackground='#454545',activeforeground='#262626')
rad_mine_to.grid(row=2,column=1,pady=2)
rad_tfc_to = tk.Radiobutton(win, text='TerraFirmaCraft', variable=rad_to, value=2,command = detect_to, fg='#dddddd',selectcolor='#535353', bg='#454545',activebackground='#454545',activeforeground='#262626')
rad_tfc_to.grid(row=3,column=1,pady=2)

rad_mine_from.bind("<Enter>", on_rad_mine_from)
rad_mine_from.bind("<Leave>", on_rad_mine_from_leave)

rad_tfc_from.bind("<Enter>", on_rad_tfc_from)
rad_tfc_from.bind("<Leave>", on_rad_tfc_from_leave)

rad_mine_to.bind("<Enter>", on_rad_mine_to)
rad_mine_to.bind("<Leave>", on_rad_mine_to_leave)

rad_tfc_to.bind("<Enter>", on_rad_tfc_to)
rad_tfc_to.bind("<Leave>", on_rad_tfc_to_leave)

from_wood_values = ('')
to_wood_values = ('')

label_wood_from = tk.Label(win, text='Replacing this wood :',bg='#454545', fg='#ffffff',font=('Arial',10,'bold')).grid(row=4,column=0)

value_in_wood_option_from = tk.StringVar(win)
value_in_wood_option_to = tk.StringVar(win)

optionmenu_wood_from = ttk.OptionMenu (win, value_in_wood_option_from, *from_wood_values)
optionmenu_wood_from.config(width=15)
optionmenu_wood_from.grid(row=4, column=1)
value_in_wood_option_from.set('Enter wood type')



label_wood_to = tk.Label(win, text='To this :',bg='#454545', fg='#ffffff',font=('Arial',10,'bold')).grid(row=5,column=0)



optionmenu_wood_to = ttk.OptionMenu (win, value_in_wood_option_to, *to_wood_values)
optionmenu_wood_to.config(width=15 )
optionmenu_wood_to.grid(row=5,column=1)
value_in_wood_option_to.set('Enter wood type')



def on_gen(e):
    bt_gen['background'] = '#262626'


def on_gen_leave(e):
    bt_gen['background'] = '#454545'

bt_gen = tk.Button(win, text='Generate', bg='#454545', fg='#ffffff',activeforeground= '#ffffff', activebackground='#262626', relief= 'flat',
				   font=('Arial',13,'bold'),bd=1,command = print_result)
bt_gen.grid(row=6, column=0,columnspan=2,pady=10)	
bt_gen.bind("<Enter>", on_gen)
bt_gen.bind("<Leave>", on_gen_leave)

text_result = tk.Text(win,height='8', width='35')
text_result.grid(row=7, column=0, columnspan=2)



def on_copy(e):
    bt_copy['background'] = '#262626'


def on_copy_leave(e):
    bt_copy['background'] = '#454545'

bt_copy = tk.Button(win,text='Copy', bg='#454545', fg='#ffffff',activeforeground= '#ffffff',font=('Arial',13,'bold'), activebackground='#262626',relief= 'flat', command = copy_result)
bt_copy.grid(row=8, column=0, columnspan=2)
bt_copy.bind("<Enter>", on_copy)
bt_copy.bind("<Leave>", on_copy_leave)

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)

win.mainloop()

