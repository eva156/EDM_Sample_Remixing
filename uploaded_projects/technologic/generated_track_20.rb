samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\technologic\samples'
use_bpm 60
downbeat_count = range(0, 150, 1)
set :downbeat_time, 1.88
define :sleep_sample_0 do |x|
	if x < 27
		if x == 0
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if (x % 4 == 0 || (x + 5) % 9 == 0 || (x + 1) % 9 == 0 || (x + 6) % 10 == 0 || (x + 2) % 10 == 0 || (x + 7) % 11 == 0)
			return true
		else 
			if false
				return false
			else 
				return false
			end
		end
	elsif x < 67
		x = (x - 67)
		return true
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 7) % 11 == 0 || x % 12 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 7) % 11 == 0 || x % 12 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 150)
		if ((x + 1) % 8 == 0 || (x + 2) % 9 == 0 || (x + 3) % 10 == 0 || (x + 4) % 11 == 0 || (x + 5) % 12 == 0 || (x + 6) % 13 == 0 || (x + 13) % 14 == 0 || (x + 7) % 14 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 7) % 11 == 0 || x % 12 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 150)
		if ((x + 1) % 8 == 0 || (x + 2) % 9 == 0 || (x + 4) % 11 == 0 || (x + 5) % 12 == 0 || (x + 7) % 14 == 0 || x % 15 == 0 || (x + 8) % 15 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		if ((x + 2) % 6 == 0 || (x + 4) % 8 == 0 || (x + 2) % 8 == 0 || x % 10 == 0 || (x + 8) % 10 == 0 || (x + 2) % 10 == 0)
			return false
		else 
			return true
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 9) % 10 == 0 || (x + 5) % 11 == 0)
			return false
		else 
			return 0
		end
	elsif x < 67
		x = (x - 67)
		if (x % 12 == 0 || x % 13 == 0 || x % 14 == 0)
			return true
		else 
			if x >= 12
				return true
			else 
				return false
			end
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 3) % 8 == 0 || (x + 1) % 8 == 0 || x % 11 == 0)
			return false
		else 
			return true
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 4) % 8 == 0 || (x + 3) % 9 == 0 || x % 10 == 0 || (x + 5) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 3) % 4 == 0 || (x + 1) % 10 == 0 || (x + 8) % 13 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		return x == 0
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		return false
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_12 do |x|
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
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_13 do |x|
	if x < 27
		if ((x + 11) % 13 == 0 || (x + 2) % 14 == 0 || (x + 14) % 16 == 0 || (x + 8) % 17 == 0)
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if (x + 5) % 12 == 0
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if 4 == x
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 3) % 8 == 0 || (x + 6) % 9 == 0 || (x + 4) % 9 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		if (x + 3) % 6 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_14 do |x|
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
		return false
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_15 do |x|
	if x < 27
		return x > 19
	elsif x < 47
		x = (x - 47)
		if (x + 1) % 3 == 0
			return false
		else 
			return 1
		end
	elsif x < 67
		x = (x - 67)
		if ((x + 4) % 7 == 0 || (x + 1) % 9 == 0 || (x + 9) % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
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
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_16 do |x|
	if x < 27
		if ((x + 7) % 17 == 0 || x % 18 == 0)
			return false
		else 
			return 0
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
		return false
	elsif x < 87
		x = (x - 87)
		return false
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_17 do |x|
	if x < 27
		if ((x + 1) % 3 == 0 || x % 14 == 0)
			return false
		else 
			return 0
		end
	elsif x < 47
		x = (x - 47)
		if x % 2 == 0
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
	elsif x < 107
		x = (x - 107)
		if ((x + 1) % 7 == 0 || (x + 7) % 10 == 0 || x % 11 == 0 || (x + 4) % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if (x % 8 == 0 || x % 11 == 0 || (x + 6) % 11 == 0)
			return false
		else 
			if false
				return false
			else 
				return true
			end
		end
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_18 do |x|
	if x < 27
		if ((x + 9) % 14 == 0 || (x + 3) % 15 == 0 || (x + 15) % 17 == 0)
			return true
		else 
			return false
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
		return false
	elsif x < 87
		x = (x - 87)
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
	elsif x < 107
		x = (x - 107)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 1) % 11 == 0 || (x + 6) % 13 == 0)
			return true
		else 
			return (1 == x || x == 4)
		end
	else 
		x = (x - 150)
		if ((x + 1) % 4 == 0 || (x + 5) % 6 == 0 || (x + 1) % 6 == 0 || (x + 7) % 8 == 0 || (x + 2) % 11 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_19 do |x|
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
		return false
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_2 do |x|
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
		return false
	elsif x < 127
		x = (x - 127)
		if x == 0
			if true
				return true
			else 
				return 1
			end
		else 
			if true
				return false
			else 
				return 1
			end
		end
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	elsif x < 67
		x = (x - 67)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if x == 0
			if false
				return false
			else 
				return true
			end
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if x == 0
			if true
				return true
			else 
				return 1
			end
		else 
			if true
				return false
			else 
				return 1
			end
		end
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
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
		x = (x - 150)
		return false
	end
end
define :sleep_sample_5 do |x|
	if x < 47
		return false
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		return false
	elsif x < 107
		x = (x - 107)
		return false
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
		x = (x - 150)
		return x == 0
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 7 == 0 || (x + 10) % 11 == 0)
			return true
		else 
			return false
		end
	elsif x < 67
		x = (x - 67)
		if x % 2 == 0
			return true
		else 
			return false
		end
	elsif x < 87
		x = (x - 87)
		if (x + 1) % 10 == 0
			return true
		else 
			if x == 0
				if true
					return true
				else 
					return false
				end
			else 
				if false
					return false
				else 
					return false
				end
			end
		end
	elsif x < 107
		x = (x - 107)
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 127
		x = (x - 127)
		if ((x + 2) % 8 == 0 || (x + 4) % 10 == 0 || (x + 10) % 11 == 0 || (x + 6) % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 150)
		if x % 2 == 1
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return (x == 0 || 23 <= x)
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return 1 <= x
	else 
		x = (x - 150)
		if ((x + 1) % 8 == 0 || (x + 2) % 9 == 0 || (x + 4) % 11 == 0 || (x + 5) % 12 == 0 || (x + 7) % 14 == 0 || x % 15 == 0 || (x + 8) % 15 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		if 20 >= x
			return false
		else 
			return true
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 8) % 9 == 0 || (x + 9) % 10 == 0 || (x + 1) % 10 == 0 || (x + 3) % 11 == 0 || (x + 5) % 12 == 0 || (x + 7) % 13 == 0)
			return false
		else 
			return 0
		end
	elsif x < 67
		x = (x - 67)
		return false
	elsif x < 87
		x = (x - 87)
		return false
	elsif x < 107
		x = (x - 107)
		return false
	elsif x < 127
		x = (x - 127)
		return false
	else 
		x = (x - 150)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		return x >= 23
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
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 6) % 10 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 9) % 13 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 150)
		return false
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 0.401, decay: 0.004, decay_level: 1.0, sustain: 1.912, sustain_level: 1.0, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0.0, attack: 0.0, attack_level: 0.476, decay: 0.011, decay_level: 1.0, sustain: 1.877, sustain_level: 1.0, release: 0.028 if sleep_sample_1(idx)
	sample samps, 2, start: 0.0, attack: 0.0, attack_level: 0.234, decay: 0.024, decay_level: 1.0, sustain: 1.88, sustain_level: 1.0, release: 0.012 if sleep_sample_10(idx)
	sample samps, 3, start: 0.0, attack: 0.0, attack_level: 0.19, decay: 0.026, decay_level: 1.0, sustain: 1.877, sustain_level: 1.0, release: 0.012 if sleep_sample_11(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.186, decay: 0.0, decay_level: 1.0, sustain: 1.873, sustain_level: 1.0, release: 0.042 if sleep_sample_12(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.246, decay: 0.026, decay_level: 1.0, sustain: 1.853, sustain_level: 1.0, release: 0.036 if sleep_sample_13(idx)
	sample samps, 6, start: 0.0, attack: 0.0, attack_level: 0.21, decay: 0.012, decay_level: 1.0, sustain: 1.892, sustain_level: 1.0, release: 0.012 if sleep_sample_14(idx)
	sample samps, 7, start: 0.0, attack: 0.0, attack_level: 0.436, decay: 0.007, decay_level: 1.0, sustain: 1.852, sustain_level: 1.0, release: 0.057 if sleep_sample_15(idx)
	sample samps, 8, start: 0.0, attack: 0.0, attack_level: 0.122, decay: 0.0, decay_level: 1.0, sustain: 1.897, sustain_level: 1.0, release: 0.019 if sleep_sample_16(idx)
	sample samps, 9, start: 0.0, attack: 0.0, attack_level: 0.183, decay: 0.0, decay_level: 1.0, sustain: 1.897, sustain_level: 1.0, release: 0.019 if sleep_sample_17(idx)
	sample samps, 10, start: 0.0, attack: 0.0, attack_level: 0.106, decay: 0.012, decay_level: 0.683, sustain: 1.859, sustain_level: 0.627, release: 0.045 if sleep_sample_18(idx)
	sample samps, 11, start: 0.0, attack: 0.0, attack_level: 0.285, decay: 0.012, decay_level: 0.944, sustain: 1.855, sustain_level: 1.0, release: 0.049 if sleep_sample_19(idx)
	sample samps, 12, start: 0.0, attack: 0.0, attack_level: 0.341, decay: 0.0, decay_level: 1.0, sustain: 1.916, sustain_level: 1.0, release: 0.0 if sleep_sample_2(idx)
	sample samps, 13, start: 0.0, attack: 0.0, attack_level: 0.368, decay: 0.003, decay_level: 1.0, sustain: 1.892, sustain_level: 1.0, release: 0.021 if sleep_sample_3(idx)
	sample samps, 14, start: 0.0, attack: 0.0, attack_level: 0.378, decay: 0.0, decay_level: 1.0, sustain: 1.877, sustain_level: 1.0, release: 0.038 if sleep_sample_4(idx)
	sample samps, 15, start: 0.0, attack: 0.0, attack_level: 0.366, decay: 0.015, decay_level: 1.0, sustain: 1.856, sustain_level: 1.0, release: 0.045 if sleep_sample_5(idx)
	sample samps, 16, start: 0.0, attack: 0.0, attack_level: 0.372, decay: 0.0, decay_level: 1.0, sustain: 1.889, sustain_level: 1.0, release: 0.026 if sleep_sample_6(idx)
	sample samps, 17, start: 0.0, attack: 0.0, attack_level: 0.21, decay: 0.0, decay_level: 1.0, sustain: 1.889, sustain_level: 1.0, release: 0.026 if sleep_sample_7(idx)
	sample samps, 18, start: 0.0, attack: 0.0, attack_level: 0.405, decay: 0.001, decay_level: 1.0, sustain: 1.875, sustain_level: 1.0, release: 0.04 if sleep_sample_8(idx)
	sample samps, 19, start: 0.0, attack: 0.0, attack_level: 0.346, decay: 0.0, decay_level: 1.0, sustain: 1.88, sustain_level: 1.0, release: 0.036 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end