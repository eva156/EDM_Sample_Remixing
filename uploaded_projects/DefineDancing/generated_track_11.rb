samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\DefineDancing\samples'
use_bpm 66
downbeat_count = range(0, 57, 1)
set :downbeat_time, 2.42
define :sleep_sample_0 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		return false
	end
end
define :sleep_sample_1 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		if ((x + 2) % 11 == 0 || (x + 6) % 13 == 0 || (x + 10) % 19 == 0 || (x + 1) % 19 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_10 do |x|
	if x < 27
		if ((x + 2) % 8 == 0 || x % 14 == 0 || (x + 11) % 17 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		if (x % 8 == 0 || (x + 5) % 8 == 0 || x % 10 == 0 || x % 12 == 0 || (x + 12) % 14 == 0 || (x + 10) % 14 == 0)
			return false
		else 
			return false
		end
	end
end
define :sleep_sample_2 do |x|
	if x < 27
		if x % 19 == 0
			return true
		else 
			return x > 19
		end
	else 
		x = (x - 57)
		if (x % 9 == 0 || x % 10 == 0 || (x + 3) % 10 == 0 || (x + 2) % 10 == 0 || (x + 1) % 10 == 0)
			return false
		else 
			return 1
		end
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		if x % 19 == 0
			return true
		else 
			return x > 19
		end
	else 
		x = (x - 57)
		if (x < 28 && x > 0)
			if x == 3
				return true
			else 
				return false
			end
		else 
			if x % 2 == 1
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
		end
	end
end
define :sleep_sample_4 do |x|
	if x < 27
		if ((x + 3) % 5 == 0 || (x + 2) % 5 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		if ((x + 3) % 4 == 0 || (x + 2) % 4 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_5 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		if ((x + 5) % 6 == 0 || (x + 3) % 6 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		if ((x + 11) % 15 == 0 || (x + 4) % 15 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		if ((x + 2) % 6 == 0 || (x + 2) % 9 == 0 || (x + 4) % 10 == 0 || (x + 6) % 11 == 0 || (x + 3) % 13 == 0 || (x + 6) % 14 == 0 || (x + 4) % 14 == 0 || (x + 16) % 19 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_7 do |x|
	if x < 27
		return x == 0
	else 
		x = (x - 57)
		return false
	end
end
define :sleep_sample_8 do |x|
	if x < 27
		if ((x + 1) % 8 == 0 || (x + 5) % 12 == 0 || (x + 6) % 13 == 0 || (x + 13) % 14 == 0 || (x + 7) % 14 == 0 || (x + 8) % 15 == 0 || (x + 10) % 17 == 0)
			return true
		else 
			if true
				return false
			else 
				return false
			end
		end
	else 
		x = (x - 57)
		if (x + 3) % 4 == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_9 do |x|
	if x < 27
		if x > 18
			return true
		else 
			return false
		end
	else 
		x = (x - 57)
		return false
	end
end
live_loop :extracted_samples do
	idx = downbeat_count.tick()
	sample samps, 0, start: 0, attack: 0, attack_level: 0.377, decay: 0, decay_level: 0.377, sustain: 2.438, sustain_level: 0.377, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0, attack: 0, attack_level: 0.446, decay: 0, decay_level: 0.446, sustain: 2.438, sustain_level: 0.446, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0, attack: 0, attack_level: 0.132, decay: 0, decay_level: 0.132, sustain: 2.438, sustain_level: 0.132, release: 0.0 if sleep_sample_10(idx)
	sample samps, 3, start: 0, attack: 0, attack_level: 0.346, decay: 0, decay_level: 0.346, sustain: 2.438, sustain_level: 0.346, release: 0.0 if sleep_sample_2(idx)
	sample samps, 4, start: 0, attack: 0, attack_level: 0.367, decay: 0, decay_level: 0.367, sustain: 2.438, sustain_level: 0.367, release: 0.0 if sleep_sample_3(idx)
	sample samps, 5, start: 0, attack: 0, attack_level: 0.304, decay: 0, decay_level: 0.304, sustain: 2.438, sustain_level: 0.304, release: 0.0 if sleep_sample_4(idx)
	sample samps, 6, start: 0, attack: 0, attack_level: 0.372, decay: 0, decay_level: 0.372, sustain: 2.438, sustain_level: 0.372, release: 0.0 if sleep_sample_5(idx)
	sample samps, 7, start: 0, attack: 0, attack_level: 0.299, decay: 0, decay_level: 0.299, sustain: 2.438, sustain_level: 0.299, release: 0.0 if sleep_sample_6(idx)
	sample samps, 8, start: 0, attack: 0, attack_level: 0.149, decay: 0, decay_level: 0.149, sustain: 2.438, sustain_level: 0.149, release: 0.0 if sleep_sample_7(idx)
	sample samps, 9, start: 0, attack: 0, attack_level: 0.396, decay: 0, decay_level: 0.396, sustain: 2.438, sustain_level: 0.396, release: 0.0 if sleep_sample_8(idx)
	sample samps, 10, start: 0, attack: 0, attack_level: 0.395, decay: 0, decay_level: 0.395, sustain: 2.438, sustain_level: 0.395, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count.tick()
	sleep get[:downbeat_time]
end