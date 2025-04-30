samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\PetiteSuit\samples'
use_bpm 67
downbeat_count = range(0, 70, 1)
set :downbeat_time, 2.57
define :sleep_sample_0 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 1) % 12 == 0 || (x + 2) % 13 == 0 || (x + 3) % 14 == 0 || (x + 4) % 15 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 3) % 4 == 0 || (x + 3) % 6 == 0 || (x + 1) % 6 == 0 || (x + 1) % 8 == 0)
			return false
		else 
			return 0
		end
	else 
		x = (x - 70)
		if 19 == x
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
define :sleep_sample_1 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 70)
		return false
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 5 == 0 || (x + 3) % 5 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 70)
		if ((x + 1) % 4 == 0 || (x + 5) % 6 == 0 || (x + 1) % 6 == 0 || (x + 7) % 8 == 0)
			return true
		else 
			return false
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
		x = (x - 70)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 70)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 8 == 0 || (x + 5) % 9 == 0 || (x + 10) % 11 == 0 || (x + 7) % 11 == 0 || (x + 8) % 12 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			return 19 == x
		end
	else 
		x = (x - 70)
		if ((x + 1) % 6 == 0 || (x + 15) % 16 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 3) % 10 == 0 || (x + 1) % 10 == 0 || (x + 9) % 12 == 0 || (x + 7) % 12 == 0 || (x + 13) % 14 == 0 || (x + 1) % 14 == 0)
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
		x = (x - 70)
		return false
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 4) % 5 == 0 || (x + 3) % 5 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 70)
		return false
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x + 4) % 5 == 0
			return true
		else 
			return false
		end
	else 
		x = (x - 70)
		return x == 0
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x % 5 == 0 || (x + 1) % 6 == 0 || (x + 1) % 8 == 0 || (x + 3) % 9 == 0 || (x + 2) % 9 == 0 || x % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 70)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		if (x + 6) % 7 == 0
			return true
		else 
			if true
				return false
			else 
				return 1
			end
		end
	else 
		x = (x - 70)
		return false
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		if x % 19 == 0
			return true
		else 
			return x > 19
		end
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 70)
		if (x + 3) % 4 == 0
			return true
		else 
			return false
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 0.363, decay: 0, decay_level: 0.363, sustain: 3.239, sustain_level: 0.363, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 1.07, decay: 0, decay_level: 1.07, sustain: 3.239, sustain_level: 1.07, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 0.56, decay: 0, decay_level: 0.56, sustain: 3.239, sustain_level: 0.56, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 0.716, decay: 0, decay_level: 0.716, sustain: 3.239, sustain_level: 0.716, release: 0.0 if sleep_sample_2(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 0.609, decay: 0, decay_level: 0.609, sustain: 3.239, sustain_level: 0.609, release: 0.0 if sleep_sample_3(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 0.6, decay: 0, decay_level: 0.6, sustain: 3.239, sustain_level: 0.6, release: 0.0 if sleep_sample_4(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 0.435, decay: 0, decay_level: 0.435, sustain: 3.239, sustain_level: 0.435, release: 0.0 if sleep_sample_5(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 0.509, decay: 0, decay_level: 0.509, sustain: 3.239, sustain_level: 0.509, release: 0.0 if sleep_sample_6(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 0.376, decay: 0, decay_level: 0.376, sustain: 3.239, sustain_level: 0.376, release: 0.0 if sleep_sample_7(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 0.433, decay: 0, decay_level: 0.433, sustain: 3.239, sustain_level: 0.433, release: 0.0 if sleep_sample_8(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 0.593, decay: 0, decay_level: 0.593, sustain: 3.239, sustain_level: 0.593, release: 0.0 if sleep_sample_9(idx)
	sample samps, 11, start: 0, attack: 0, attack_level: 0.437, decay: 0, decay_level: 0.437, sustain: 3.239, sustain_level: 0.437, release: 0.0 if sleep_sample_11(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end