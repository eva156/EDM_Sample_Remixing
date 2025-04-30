samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\TheBirds\samples'
use_bpm 60
downbeat_count = range(0, 69, 1)
set :downbeat_time, 3.53
define :sleep_sample_0 do |x|
	if x < 27
		if ((x + 3) % 5 == 0 || (x + 2) % 5 == 0 || x % 17 == 0)
			return false
		else 
			return 0
		end
	elsif x < 47
		x = (x - 47)
		if ((x + 2) % 8 == 0 || (x + 4) % 10 == 0 || (x + 10) % 11 == 0 || (x + 6) % 12 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 69)
		if ((x + 6) % 7 == 0 || (x + 1) % 8 == 0 || (x + 12) % 13 == 0 || x % 14 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_1 do |x|
	if x < 47
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_11 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 9) % 10 == 0 || (x + 1) % 12 == 0 || (x + 3) % 14 == 0)
			return true
		else 
			if true
				return false
			else 
				return 0
			end
		end
	elsif x < 47
		x = (x - 47)
		return 1 == x
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_2 do |x|
	if x < 47
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		if ((x + 5) % 8 == 0 || (x + 1) % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_4 do |x|
	if x < 47
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		if ((x + 3) % 6 == 0 || (x + 6) % 9 == 0 || (x + 3) % 9 == 0 || (x + 6) % 12 == 0)
			return true
		else 
			return false
		end
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_7 do |x|
	if x < 47
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 69)
		return false
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		return false
	elsif x < 47
		x = (x - 47)
		return false
	else 
		x = (x - 69)
		if ((x + 7) % 8 == 0 || (x + 6) % 10 == 0 || (x + 7) % 11 == 0 || (x + 2) % 11 == 0 || (x + 3) % 12 == 0 || (x + 10) % 14 == 0)
			return true
		else 
			if true
				return false
			else 
				return 1
			end
		end
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 0.767, decay: 0, decay_level: 0.767, sustain: 4.365, sustain_level: 0.767, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 4.365, sustain_level: 1.0, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 0.405, decay: 0, decay_level: 0.405, sustain: 4.365, sustain_level: 0.405, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 0.378, decay: 0, decay_level: 0.378, sustain: 4.365, sustain_level: 0.378, release: 0.0 if sleep_sample_11(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 0.701, decay: 0, decay_level: 0.701, sustain: 4.365, sustain_level: 0.701, release: 0.0 if sleep_sample_2(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 0.857, decay: 0, decay_level: 0.857, sustain: 4.365, sustain_level: 0.857, release: 0.0 if sleep_sample_3(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 0.737, decay: 0, decay_level: 0.737, sustain: 4.365, sustain_level: 0.737, release: 0.0 if sleep_sample_4(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 0.696, decay: 0, decay_level: 0.696, sustain: 4.365, sustain_level: 0.696, release: 0.0 if sleep_sample_5(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 0.492, decay: 0, decay_level: 0.492, sustain: 4.365, sustain_level: 0.492, release: 0.0 if sleep_sample_6(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 0.641, decay: 0, decay_level: 0.641, sustain: 4.365, sustain_level: 0.641, release: 0.0 if sleep_sample_7(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 0.618, decay: 0, decay_level: 0.618, sustain: 4.365, sustain_level: 0.618, release: 0.0 if sleep_sample_8(idx)
	sample samps, 11, start: 0, attack: 0, attack_level: 0.474, decay: 0, decay_level: 0.474, sustain: 4.365, sustain_level: 0.474, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end