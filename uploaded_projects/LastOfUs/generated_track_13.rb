samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\LastOfUs\samples'
use_bpm 51
downbeat_count = range(0, 76, 1)
set :downbeat_time, 2.33
define :sleep_sample_0 do |x|
	if x < 27
		if ((x + 5) % 12 == 0 || (x + 1) % 14 == 0 || (x + 9) % 16 == 0 || (x + 17) % 18 == 0)
			return true
		else 
			if true
				return false
			else 
				return 1
			end
		end
	elsif x < 47
		x = (x - 47)
		if x % 3 == 0
			return false
		else 
			return 0
		end
	else 
		x = (x - 76)
		return true
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 8 == 0 || x % 10 == 0 || (x + 8) % 10 == 0 || (x + 4) % 12 == 0 || (x + 8) % 14 == 0)
			return false
		else 
			return 1
		end
	else 
		x = (x - 76)
		if ((x + 1) % 6 == 0 || (x + 4) % 9 == 0 || (x + 10) % 11 == 0 || (x + 2) % 11 == 0 || (x + 6) % 12 == 0 || (x + 4) % 12 == 0 || (x + 13) % 14 == 0 || (x + 11) % 14 == 0)
			return false
		else 
			return true
		end
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		if x % 2 == 1
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if (x % 4 == 0 || (x + 4) % 6 == 0 || (x + 2) % 6 == 0 || (x + 2) % 8 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		if x == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		if (x % 6 == 0 || (x + 1) % 6 == 0 || (x + 2) % 14 == 0)
			return false
		else 
			return 1
		end
	elsif x < 47
		x = (x - 47)
		if x % 2 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		if (x + 1) % 3 == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_12 do |x|
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
		if x % 2 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		if ((x + 3) % 8 == 0 || (x + 7) % 12 == 0 || (x + 3) % 12 == 0 || (x + 15) % 16 == 0)
			return true
		else 
			if true
				return false
			else 
				return false
			end
		end
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 76)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		if ((x + 6) % 8 == 0 || (x + 4) % 10 == 0 || (x + 2) % 10 == 0 || (x + 10) % 12 == 0 || (x + 8) % 12 == 0 || x % 14 == 0 || (x + 2) % 14 == 0)
			return false
		else 
			if false
				return false
			else 
				return 0
			end
		end
	elsif x < 47
		x = (x - 47)
		if x % 2 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 76)
		return false
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		if (x % 3 == 0 || (x + 1) % 13 == 0)
			return true
		else 
			if false
				return 1
			else 
				return false
			end
		end
	elsif x < 47
		x = (x - 47)
		if (x + 4) % 5 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		return false
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x % 7 == 0 || (x + 4) % 8 == 0 || (x + 4) % 9 == 0 || x % 11 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		if ((x + 1) % 3 == 0 || (x + 2) % 13 == 0 || (x + 6) % 14 == 0 || (x + 3) % 14 == 0 || (x + 5) % 16 == 0 || (x + 6) % 17 == 0)
			return false
		else 
			return 0
		end
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if x % 2 == 1
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		if ((x + 3) % 4 == 0 || (x + 5) % 14 == 0 || (x + 1) % 14 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		if ((x + 7) % 8 == 0 || (x + 1) % 10 == 0 || (x + 2) % 11 == 0 || (x + 3) % 12 == 0 || (x + 4) % 13 == 0 || (x + 6) % 15 == 0 || (x + 8) % 17 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 9 == 0 || (x + 9) % 10 == 0 || (x + 6) % 11 == 0 || (x + 2) % 11 == 0 || (x + 10) % 13 == 0)
			return false
		else 
			return 1
		end
	else 
		x = (x - 76)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 8 == 0 || (x + 4) % 10 == 0 || (x + 10) % 11 == 0 || (x + 6) % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 76)
		return 20 < x
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 0.346, decay: 0, decay_level: 0.346, sustain: 2.345, sustain_level: 0.346, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 0.43, decay: 0, decay_level: 0.43, sustain: 2.345, sustain_level: 0.43, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 0.359, decay: 0, decay_level: 0.359, sustain: 2.345, sustain_level: 0.359, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 0.296, decay: 0, decay_level: 0.296, sustain: 2.345, sustain_level: 0.296, release: 0.0 if sleep_sample_11(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 0.157, decay: 0, decay_level: 0.157, sustain: 2.345, sustain_level: 0.157, release: 0.0 if sleep_sample_12(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 0.367, decay: 0, decay_level: 0.367, sustain: 2.345, sustain_level: 0.367, release: 0.0 if sleep_sample_2(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 0.351, decay: 0, decay_level: 0.351, sustain: 2.345, sustain_level: 0.351, release: 0.0 if sleep_sample_3(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 0.292, decay: 0, decay_level: 0.292, sustain: 2.345, sustain_level: 0.292, release: 0.0 if sleep_sample_4(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 0.453, decay: 0, decay_level: 0.453, sustain: 2.345, sustain_level: 0.453, release: 0.0 if sleep_sample_5(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 0.419, decay: 0, decay_level: 0.419, sustain: 2.345, sustain_level: 0.419, release: 0.0 if sleep_sample_6(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 0.21, decay: 0, decay_level: 0.21, sustain: 2.345, sustain_level: 0.21, release: 0.0 if sleep_sample_7(idx)
	sample samps, 11, start: 0, attack: 0, attack_level: 0.216, decay: 0, decay_level: 0.216, sustain: 2.345, sustain_level: 0.216, release: 0.0 if sleep_sample_8(idx)
	sample samps, 12, start: 0, attack: 0, attack_level: 0.225, decay: 0, decay_level: 0.225, sustain: 2.345, sustain_level: 0.225, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end