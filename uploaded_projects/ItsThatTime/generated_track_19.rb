samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\ItsThatTime\samples'
use_bpm 60
#downbeat_count = (ring 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144)
downbeat_count = range(0, 144, 1)
define :sleep_sample_0 do |x|
	if x < 27
		if ((x + 4) % 7 == 0 || x % 17 == 0)
			return false
		else 
			return 0
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 8 == 0 || (x + 4) % 9 == 0 || (x + 6) % 10 == 0 || (x + 8) % 11 == 0 || (x + 10) % 12 == 0 || (x + 12) % 13 == 0 || (x + 6) % 13 == 0)
			return false
		else 
			return true
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 5) % 8 == 0 || (x + 1) % 10 == 0 || x % 11 == 0 || (x + 5) % 12 == 0 || (x + 9) % 14 == 0)
			return false
		else 
			return not(false)
		end
	elsif x < 87
		x = (x - 87)
		if (x + 6) % 7 == 0
			return false
		else 
			return 1
		end
	elsif x < 107
		x = (x - 107)
		if (x % 11 == 0 || (x + 5) % 11 == 0)
			return false
		else 
			return 0
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 9) % 10 == 0 || (x + 4) % 11 == 0 || (x + 2) % 11 == 0 || (x + 8) % 13 == 0)
			return false
		else 
			if 3 == x
				if true
					return false
				else 
					return false
				end
			else 
				return 1
			end
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if x < 26
			if true
				return false
			else 
				return false
			end
		else 
			if false
				return false
			else 
				return true
			end
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 8 == 0 || (x + 3) % 8 == 0 || (x + 6) % 9 == 0 || (x + 4) % 9 == 0 || (x + 8) % 10 == 0 || (x + 5) % 10 == 0 || (x + 10) % 11 == 0 || (x + 6) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if (x + 7) % 8 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 4) % 8 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 4) % 9 == 0 || (x + 10) % 11 == 0 || (x + 6) % 11 == 0 || (x + 8) % 13 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 145)
		return x == 0
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if x % 2 == 0
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if x == 19
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 10) % 11 == 0 || (x + 6) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if x % 3 == 0
			return false
		else 
			return 1
		end
	elsif x < 107
		x = (x - 107)
		if x % 3 == 0
			return false
		else 
			return 1
		end
	elsif x < 127
		x = (x - 127)
		if x == 19
			return true
		else 
			return false
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_12 do |x|
	if x < 27
		if ((x + 9) % 14 == 0 || (x + 3) % 14 == 0 || (x + 4) % 15 == 0 || (x + 15) % 17 == 0 || (x + 12) % 17 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if x % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_13 do |x|
	if x < 27
		if x == 0
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 1) % 8 == 0 || (x + 2) % 9 == 0 || (x + 3) % 10 == 0 || (x + 11) % 12 == 0 || (x + 12) % 13 == 0)
			return false
		else 
			return 1
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 1) % 13 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			if 14 > x
				if true
					return false
				else 
					return false
				end
			else 
				return true
			end
		end
	elsif x < 87
		x = (x - 87)
		if not(2 >= x)
			if x <= 17
				return false
			else 
				return true
			end
		else 
			return true
		end
	elsif x < 107
		x = (x - 107)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 3) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 1) % 8 == 0)
			return false
		else 
			return 0
		end
	else 
		x = (x - 145)
		if ((x + 1) % 11 == 0 || (x + 1) % 12 == 0)
			return true
		else 
			if 12 > x
				return false
			else 
				return true
			end
		end
	end
end
define :sleep_sample_14 do |x|
	if x < 27
		if (x % 4 == 0 || x % 6 == 0 || (x + 2) % 6 == 0 || (x + 2) % 8 == 0 || (x + 8) % 10 == 0)
			return false
		else 
			return 0
		end
	elsif x < 47
		x = (x - 47)
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 6 == 0 || (x + 4) % 8 == 0 || (x + 2) % 8 == 0 || x % 10 == 0)
			return false
		else 
			return true
		end
	elsif x < 87
		x = (x - 87)
		if x % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 7) % 9 == 0 || (x + 6) % 11 == 0 || (x + 4) % 12 == 0)
			return false
		else 
			return true
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_15 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if ((x + 1) % 13 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			if 14 > x
				if true
					return false
				else 
					return false
				end
			else 
				return true
			end
		end
	elsif x < 87
		x = (x - 87)
		if (x % 10 == 0 || (x + 3) % 10 == 0 || x % 11 == 0 || (x + 5) % 11 == 0 || (x + 4) % 11 == 0)
			return false
		else 
			return 0
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_16 do |x|
	if x < 27
		if ((x + 4) % 7 == 0 || (x + 9) % 13 == 0 || (x + 2) % 13 == 0 || (x + 10) % 14 == 0 || (x + 13) % 15 == 0 || (x + 15) % 16 == 0 || x % 17 == 0)
			return false
		else 
			return 25373 > 25347
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 1) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 3) % 8 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 3) % 8 == 0 || (x + 2) % 11 == 0 || (x + 7) % 12 == 0 || x % 13 == 0)
			return false
		else 
			return 1
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 1) % 6 == 0 || (x + 7) % 8 == 0 || (x + 4) % 9 == 0 || (x + 3) % 10 == 0 || (x + 8) % 11 == 0)
			return false
		else 
			return true
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 1) % 13 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			if 14 > x
				if true
					return false
				else 
					return false
				end
			else 
				return true
			end
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 1) % 7 == 0 || (x + 7) % 9 == 0 || (x + 5) % 9 == 0 || (x + 9) % 10 == 0 || (x + 7) % 10 == 0 || (x + 2) % 11 == 0 || (x + 1) % 11 == 0 || (x + 4) % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_17 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if (x + 1) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 3) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 1) % 8 == 0)
			return false
		else 
			return 0
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		if ((x + 9) % 10 == 0 || (x + 2) % 10 == 0 || (x + 8) % 13 == 0)
			return false
		else 
			return true
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_18 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x + 6) % 7 == 0
			return false
		else 
			return 1
		end
	elsif x < 67
		x = (x - 67)
		if x % 5 == 0
			return false
		else 
			return 1
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 2) % 4 == 0 || (x + 1) % 4 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if (x % 5 == 0 || (x + 2) % 5 == 0)
			return false
		else 
			return 1
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 5) % 6 == 0 || (x + 1) % 8 == 0 || (x + 6) % 9 == 0 || (x + 2) % 9 == 0 || (x + 3) % 10 == 0 || (x + 8) % 11 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 9) % 10 == 0 || (x + 1) % 12 == 0 || (x + 3) % 14 == 0 || (x + 4) % 15 == 0 || (x + 14) % 17 == 0 || (x + 16) % 19 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return x > 13
	else 
		x = (x - 145)
		if ((x + 1) % 5 == 0 || x % 9 == 0)
			return false
		else 
			return 0
		end
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if x % 3 == 0
			return false
		else 
			return 1
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 1) % 6 == 0 || x % 7 == 0 || (x + 7) % 9 == 0 || (x + 2) % 11 == 0)
			return false
		else 
			return true
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 1) % 13 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			if 14 > x
				if true
					return false
				else 
					return false
				end
			else 
				return true
			end
		end
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if (x % 9 == 0 || x % 10 == 0 || (x + 2) % 10 == 0 || (x + 1) % 10 == 0 || (x + 4) % 14 == 0 || (x + 5) % 15 == 0 || (x + 6) % 16 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if (x % 12 == 0 || x % 13 == 0 || x % 14 == 0)
			return true
		else 
			if x >= 12
				return true
			else 
				return false
			end
		end
	elsif x < 67
		x = (x - 67)
		if (x % 3 == 0 || (x + 4) % 10 == 0 || (x + 1) % 10 == 0 || (x + 5) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if (x % 3 == 0 || (x + 1) % 10 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return true
	elsif x < 127
		x = (x - 127)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	else 
		x = (x - 145)
		if ((x + 5) % 6 == 0 || (x + 5) % 8 == 0 || (x + 3) % 8 == 0 || (x + 1) % 10 == 0)
			return false
		else 
			return 1
		end
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		if x == 0
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 3) % 5 == 0 || x % 7 == 0 || (x + 1) % 8 == 0 || (x + 2) % 9 == 0 || (x + 9) % 11 == 0 || (x + 4) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		return true
	elsif x < 107
		x = (x - 107)
		if (x % 10 == 0 || x % 11 == 0 || (x + 2) % 11 == 0 || x % 12 == 0 || (x + 4) % 12 == 0 || x % 13 == 0 || (x + 6) % 13 == 0)
			return false
		else 
			return 61404 % 4 == 0
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 7) % 11 == 0 || x % 12 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return 32784 == 28662
		end
	else 
		x = (x - 145)
		return x == 0
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return 1 <= x
	elsif x < 67
		x = (x - 67)
		if ((x + 1) % 13 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			if 14 > x
				if true
					return false
				else 
					return false
				end
			else 
				return true
			end
		end
	elsif x < 87
		x = (x - 87)
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return x > 13
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 6) % 9 == 0 || (x + 5) % 9 == 0 || (x + 8) % 10 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	else 
		x = (x - 145)
		return false
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if x == 18
			return false
		else 
			if false
				return false
			else 
				return false
			end
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 6) % 9 == 0 || (x + 1) % 11 == 0)
			return true
		else 
			if 18 == x
				if false
					return false
				else 
					return true
				end
			else 
				return false
			end
		end
	elsif x < 87
		x = (x - 87)
		if (x + 2) % 3 == 0
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 4) % 5 == 0 || (x + 1) % 5 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 5) % 11 == 0 || x % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 145)
		if ((x + 1) % 11 == 0 || (x + 9) % 12 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		if ((x + 1) % 10 == 0 || (x + 2) % 11 == 0 || (x + 3) % 12 == 0 || (x + 15) % 16 == 0 || (x + 16) % 17 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if ((x + 6) % 9 == 0 || (x + 2) % 9 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 145)
		return false
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 1.234, decay: 0, decay_level: 1.234, sustain: 1.637, sustain_level: 1.234, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_11(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 1.004, decay: 0, decay_level: 1.004, sustain: 1.637, sustain_level: 1.004, release: 0.0 if sleep_sample_12(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 1.135, decay: 0, decay_level: 1.135, sustain: 1.637, sustain_level: 1.135, release: 0.0 if sleep_sample_13(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_14(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_15(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_16(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_17(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_18(idx)
	sample samps, 11, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_2(idx)
	sample samps, 12, start: 0, attack: 0, attack_level: 1.043, decay: 0, decay_level: 1.043, sustain: 1.637, sustain_level: 1.043, release: 0.0 if sleep_sample_3(idx)
	sample samps, 13, start: 0, attack: 0, attack_level: 1.302, decay: 0, decay_level: 1.302, sustain: 1.637, sustain_level: 1.302, release: 0.0 if sleep_sample_4(idx)
	sample samps, 14, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_5(idx)
	sample samps, 15, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_6(idx)
	sample samps, 16, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0 if sleep_sample_7(idx)
	sample samps, 17, start: 0, attack: 0, attack_level: 1.073, decay: 0, decay_level: 1.073, sustain: 1.637, sustain_level: 1.073, release: 0.0 if sleep_sample_8(idx)
	sample samps, 18, start: 0, attack: 0, attack_level: 1.035, decay: 0, decay_level: 1.035, sustain: 1.637, sustain_level: 1.035, release: 0.0 if sleep_sample_9(idx)
	sleep 1.63
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep 1.63
end