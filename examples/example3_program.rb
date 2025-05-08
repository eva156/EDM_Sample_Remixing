samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project\EDM_Sample_Remixing\uploaded_projects\BadParentingFunk\samples'
use_bpm 59
downbeat_count_extracted = range(0, 51, 1)
downbeat_count_sonic = range(0, 51, 1)
set :downbeat_time, 1.7
define :sleep_sample_0 do |x|
	if (x < 7)
		return false
	end
	if ((x + 7) % 10 == 0 || (x + 6) % 10 == 0 || (x + 11) % 18 == 0 || (x + 3) % 18 == 0 || (x + 5) % 20 == 0 || (x + 19) % 21 == 0 || (x + 18) % 21 == 0 || (x + 21) % 23 == 0 || (x + 15) % 24 == 0 || (x + 17) % 25 == 0 || (x + 1) % 25 == 0 || (x + 2) % 26 == 0)
		return true
	else 
		return false
	end
end
define :sleep_sample_1 do |x|
	if (x >= 47 || (x + 5) % 8 == 0 || (x + 23) % 25 == 0 || (x + 6) % 25 == 0)
		return true
	else 
		return false
	end
end
define :sleep_sample_2 do |x|
	if x < 7
		return false
	end
	if (x >= 42 || x % 3 == 0)
		return false
	else 
		return true
	end
end
define :sleep_sample_3 do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		if ((x >= 16 && x <= 22) || (x + 8) % 9 == 0 || (x + 8) % 12 == 0 || (x + 3) % 13 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_4 do |x|
	return false
end
define :sleep_sample_5 do |x|
	if ((x + 5) % 16 == 0 || (x + 13) % 24 == 0 || (x + 5) % 24 == 0 || (x + 10) % 29 == 0 || (x + 27) % 31 == 0)
		return true
	else 
		return false
	end
end
define :sleep_sample_6 do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		if ((x + 3) % 7 == 0 || (x + 2) % 7 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_sample_7 do |x|
	if ((x + 5) % 14 == 0 || (x + 4) % 14 == 0 || (x + 3) % 20 == 0 || (x + 12) % 21 == 0 || (x + 11) % 21 == 0 || (x + 5) % 21 == 0 || (x + 10) % 27 == 0 || (x + 11) % 28 == 0)
		return true
	else 
		return false
	end
end
define :sleep_sample_8 do |x|
	if x < 7
		return false
	end
	if ((x + 7) % 10 == 0 || (x + 7) % 15 == 0 || (x + 2) % 15 == 0 || (x + 2) % 20 == 0 || (x + 21) % 22 == 0 || (x + 1) % 24 == 0 || (x + 3) % 26 == 0)
		return true
	else 
		return false
	end
end
define :sleep_sample_9 do |x|
	if ((x + 3) % 16 == 0 || (x + 15) % 22 == 0 || (x + 8) % 22 == 0 || (x + 9) % 23 == 0 || (x + 12) % 24 == 0 || (x + 10) % 24 == 0 || (x + 3) % 24 == 0 || x % 27 == 0 || x % 28 == 0)
		return true
	else 
		return false
	end
end
define :sleep_loop_garzul do |x|
	if x <= 7
		return false
	end
	if ((x + 2) % 7 == 0 || (x + 8) % 14 == 0 || (x + 6) % 14 == 0 || (x + 5) % 14 == 0)
		return false
	else 
		return true
	end
end
define :sleep_drum_roll do |x|
	if x < 27
		if (x + 1) % 3 == 0
			return false
		else 
			return true
		end
	else 
		x = (x - 27)
		if x % 2 == 0
			return true
		else 
			return false
		end
	end
end
define :sleep_bass_voxy_c do |x|
	if x >= 7 && x <= 27
		return true
	else 
		return false
	end
end
define :sleep_loop_mehackit1 do |x|
	if x % 2 == 1 || x == 0
		return false
	else 
		return true
	end
end
define :sleep_loop_compus do |x|
	if x < 27
		if (x >= 19 || x % 19 == 0)
			return true
		else 
			return false
		end
	else 
		x = (x - 27)
		if ((x + 5) % 8 == 0 || (x + 4) % 10 == 0 || x % 11 == 0)
			return true
		else 
			return false
		end
	end
end
define :sleep_drum_splash_hard do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		return false
	end
end
define :sleep_loop_mehackit2 do |x|
	if x < 27
		return false
	else 
		x = (x - 27)
		return 1 > x
	end
end
define :sleep_bass_drop_c do |x|
	if x % 2 == 1
		return false
	else 
		return true
	end
end
define :sleep_loop_weirdo do |x|
	if ((x + 1) % 4 == 0 || x % 27 == 0)
		return true
	else 
		return false
	end
end
define :sleep_mehackit_phone3 do |x|
	if x == 0
		return false
	end
	if ((x + 8) % 10 == 0 || (x + 8) % 12 == 0 || (x + 6) % 12 == 0 || x % 14 == 0 || (x + 4) % 14 == 0 || (x + 2) % 14 == 0 || (x + 12) % 16 == 0 || (x + 8) % 16 == 0 || (x + 2) % 18 == 0)
		return true
	else 
		return false
	end
end
define :sleep_loop_electric do |x|
	if 7 == x
		return true
	else 
		return false
	end
end
live_loop :extracted_samples do
	idx = downbeat_count_extracted.tick()
	sample samps, 0, start: 0.0, attack: 0.0, attack_level: 0.537, decay: 0.0, decay_level: 0.537, sustain: 1.741, sustain_level: 0.537, release: 0.0 if sleep_sample_0(idx)
	sample samps, 1, start: 0.0, attack: 0.0, attack_level: 0.395, decay: 0.0, decay_level: 0.395, sustain: 1.741, sustain_level: 0.395, release: 0.0 if sleep_sample_1(idx)
	sample samps, 2, start: 0.0, attack: 0.0, attack_level: 0.5, decay: 0.0, decay_level: 0.5, sustain: 1.741, sustain_level: 0.5, release: 0.0 if sleep_sample_2(idx)
	sample samps, 3, start: 0.0, attack: 0.0, attack_level: 0.526, decay: 0.0, decay_level: 0.526, sustain: 1.741, sustain_level: 0.526, release: 0.0 if sleep_sample_3(idx)
	sample samps, 4, start: 0.0, attack: 0.0, attack_level: 0.536, decay: 0.0, decay_level: 0.536, sustain: 1.741, sustain_level: 0.536, release: 0.0 if sleep_sample_4(idx)
	sample samps, 5, start: 0.0, attack: 0.0, attack_level: 0.206, decay: 0.0, decay_level: 0.206, sustain: 1.741, sustain_level: 0.206, release: 0.0 if sleep_sample_5(idx)
	sample samps, 6, start: 0.0, attack: 0.0, attack_level: 0.426, decay: 0.0, decay_level: 0.426, sustain: 1.741, sustain_level: 0.426, release: 0.0 if sleep_sample_6(idx)
	sample samps, 7, start: 0.0, attack: 0.0, attack_level: 0.58, decay: 0.0, decay_level: 0.58, sustain: 1.741, sustain_level: 0.58, release: 0.0 if sleep_sample_7(idx)
	sample samps, 8, start: 0.0, attack: 0.0, attack_level: 0.39, decay: 0.0, decay_level: 0.39, sustain: 1.741, sustain_level: 0.39, release: 0.0 if sleep_sample_8(idx)
	sample samps, 9, start: 0.0, attack: 0.0, attack_level: 0.444, decay: 0.0, decay_level: 0.444, sustain: 1.741, sustain_level: 0.444, release: 0.0 if sleep_sample_9(idx)
	sleep get[:downbeat_time]
end
live_loop :sonic_pi_samples do
	idx = downbeat_count_sonic.tick()
	sample :loop_garzul, start: 0.0, attack: 0.0, attack_level: 0.407, decay: 1.168, decay_level: 0.306, sustain: 0.799, sustain_level: 0.0, release: 1.99 if sleep_loop_garzul(idx)
	sample :drum_roll, start: 0.0, attack: 0.0, attack_level: 0.312, decay: 0.323, decay_level: 0.211, sustain: 0.062, sustain_level: 0.0, release: 5.856 if sleep_drum_roll(idx)
	sample :bass_voxy_c, start: 0.0, attack: 0.0, attack_level: 0.112, decay: 0.887, decay_level: 0.162, sustain: 0.854, sustain_level: 0.0, release: 4.494 if sleep_bass_voxy_c(idx)
	#sample :loop_mehackit1, start: 0.0, attack: 1.379, attack_level: 0.0, decay: 0.017, decay_level: 0.51, sustain: 0.72, sustain_level: 0.584, release: 0.359 if sleep_loop_mehackit1(idx)
	sample :loop_compus, start: 0.408, attack: 0.193, attack_level: 1.064, decay: 0.313, decay_level: 1.031, sustain: 0.078, sustain_level: 0.0, release: 5.495 if sleep_loop_compus(idx)
	sample :drum_splash_hard, start: 0.0, attack: 0.0, attack_level: 0.931, decay: 0.168, decay_level: 0.715, sustain: 2.189, sustain_level: 0.549, release: 0.238 if sleep_drum_splash_hard(idx)
	sample :loop_mehackit2, start: 0.0, attack: 0.0, attack_level: 0.802, decay: 0.499, decay_level: 0.543, sustain: 0.411, sustain_level: 0.0, release: 1.565 if sleep_loop_mehackit2(idx)
	#sample :bass_drop_c, start: 0.0, attack: 0.0, attack_level: 0.389, decay: 0.208, decay_level: 0.355, sustain: 1.874, sustain_level: 0.0, release: 0.277 if sleep_bass_drop_c(idx)
	sample :loop_weirdo, start: 0.0, attack: 0.212, attack_level: 0.555, decay: 0.318, decay_level: 0.555, sustain: 1.136, sustain_level: 0.0, release: 3.283 if sleep_loop_weirdo(idx)
	sample :mehackit_phone3, start: 0.0, attack: 0.0, attack_level: 0.382, decay: 0.199, decay_level: 0.316, sustain: 1.633, sustain_level: 0.308, release: 0.005 if sleep_mehackit_phone3(idx)
	sample :loop_electric, start: 0.0, attack: 0.0, attack_level: 0.735, decay: 0.161, decay_level: 0.464, sustain: 2.303, sustain_level: 0.606, release: 0.01 if sleep_loop_electric(idx)
	sleep get[:downbeat_time]
end