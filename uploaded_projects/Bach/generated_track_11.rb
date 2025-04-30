samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\Bach\samples'
use_bpm 67
downbeat_count = range(0, 61, 1)
set :downbeat_time, 2.38
define :sleep_sample_0 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x % 5 == 0 || (x + 2) % 5 == 0)
			return false
		else 
			return 0
		end
	else 
		x = (x - 61)
		if ((x + 1) % 3 == 0 || x % 8 == 0)
			return false
		else 
			return 0
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if ((x + 2) % 8 == 0 || (x + 5) % 11 == 0 || (x + 3) % 11 == 0 || (x + 2) % 12 == 0 || x % 14 == 0 || (x + 11) % 14 == 0 || (x + 3) % 15 == 0)
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
	else 
		x = (x - 61)
		if (x + 4) % 9 == 0
			return false
		else 
			if x > 5
				if false
					return false
				else 
					return 1
				end
			else 
				return false
			end
		end
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 61)
		if ((x + 5) % 6 == 0 || (x + 1) % 7 == 0 || (x + 7) % 8 == 0 || (x + 8) % 9 == 0)
			return true
		else 
			return x >= 12
		end
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 5) % 7 == 0 || (x + 4) % 9 == 0 || (x + 2) % 9 == 0 || (x + 8) % 10 == 0 || (x + 4) % 11 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 61)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		if x % 19 == 0
			return true
		else 
			return x > 19
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 4 == 0 || (x + 4) % 6 == 0 || (x + 2) % 6 == 0 || (x + 4) % 8 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 61)
		if ((x + 1) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 7) % 8 == 0)
			return true
		else 
			if true
				return false
			else 
				return 0
			end
		end
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if ((x + 1) % 13 == 0 || (x + 9) % 14 == 0 || (x + 12) % 17 == 0 || x % 19 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 4 == 0 || (x + 4) % 6 == 0 || (x + 2) % 6 == 0 || (x + 4) % 8 == 0 || (x + 10) % 11 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 61)
		return x == 0
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x + 5) % 6 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 61)
		if ((x + 5) % 6 == 0 || (x + 8) % 9 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 8) % 10 == 0 || (x + 10) % 11 == 0 || (x + 9) % 11 == 0)
			return true
		else 
			if 17 >= x
				return false
			else 
				return true
			end
		end
	else 
		x = (x - 61)
		if ((x + 2) % 4 == 0 || (x + 1) % 4 == 0 || (x + 1) % 7 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 61)
		if x % 2 == 1
			return true
		else 
			return false
		end
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
		if ((x + 4) % 6 == 0 || (x + 3) % 6 == 0)
			return false
		else 
			return 1
		end
	else 
		x = (x - 61)
		if x % 2 == 1
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		if (x + 5) % 8 == 0
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 5) % 8 == 0 || (x + 8) % 11 == 0 || (x + 3) % 11 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 61)
		if (x + 4) % 9 == 0
			return false
		else 
			if x > 5
				if false
					return false
				else 
					return 1
				end
			else 
				return false
			end
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 0.402, decay: 0, decay_level: 0.402, sustain: 2.519, sustain_level: 0.402, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 0.433, decay: 0, decay_level: 0.433, sustain: 2.519, sustain_level: 0.433, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 0.363, decay: 0, decay_level: 0.363, sustain: 2.519, sustain_level: 0.363, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 0.499, decay: 0, decay_level: 0.499, sustain: 2.519, sustain_level: 0.499, release: 0.0 if sleep_sample_2(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 0.491, decay: 0, decay_level: 0.491, sustain: 2.519, sustain_level: 0.491, release: 0.0 if sleep_sample_3(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 0.284, decay: 0, decay_level: 0.284, sustain: 2.519, sustain_level: 0.284, release: 0.0 if sleep_sample_4(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 0.503, decay: 0, decay_level: 0.503, sustain: 2.519, sustain_level: 0.503, release: 0.0 if sleep_sample_5(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 0.425, decay: 0, decay_level: 0.425, sustain: 2.519, sustain_level: 0.425, release: 0.0 if sleep_sample_6(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 0.579, decay: 0, decay_level: 0.579, sustain: 2.519, sustain_level: 0.579, release: 0.0 if sleep_sample_7(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 0.173, decay: 0, decay_level: 0.173, sustain: 2.519, sustain_level: 0.173, release: 0.0 if sleep_sample_8(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 0.459, decay: 0, decay_level: 0.459, sustain: 2.519, sustain_level: 0.459, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end