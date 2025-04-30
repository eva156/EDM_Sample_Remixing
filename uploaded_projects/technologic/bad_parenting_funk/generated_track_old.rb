samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\bad_parenting_funk\samples'
use_bpm 60.09265988372093
set :max_time, 220.12696145124715
live_loop :start do
	sleep get[:max_time]
	cue 'start'
end
sleep_sample_0_0 = (ring 52.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.01,4.01,4.0,4.0,4.01,3.98,4.0,4.0,3.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,8.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,-1)
live_loop :loop_sample_0_0 do
	sleep_time = sleep_sample_0_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 0, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_0_1 = (ring 54.0,8.0,4.0,4.0,4.0,4.0,4.02,3.99,4.01,4.0,4.0,4.0,4.0,3.99,7.99,8.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,12.0,8.0,4.0,4.0,4.0,4.0,-1)
live_loop :loop_sample_0_1 do
	sleep_time = sleep_sample_0_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 0, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_1_0 = (ring 20.01,4.0,4.0,4.0,4.0,4.0,4.0,27.99,12.01,4.01,4.0,4.0,4.01,3.98,58.0,21.99,4.0,10.0,4.0,4.0,4.01,-1)
live_loop :loop_sample_1_0 do
	sleep_time = sleep_sample_1_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 1, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_1_1 = (ring 22.01,8.0,8.0,8.0,40.0,78.0,36.0,3.99,4.01,3.99,-1)
live_loop :loop_sample_1_1 do
	sleep_time = sleep_sample_1_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 1, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_10_0 = (ring 28.01,8.0,4.0,4.0,4.03,3.96,4.0,4.0,4.0,52.0,4.0,4.0,4.0,22.0,8.0,10.0,4.0,4.0,4.0,4.0,8.0,6.0,8.0,-1)
live_loop :loop_sample_10_0 do
	sleep_time = sleep_sample_10_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 2, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_10_1 = (ring 208.01,-1)
live_loop :loop_sample_10_1 do
	sleep_time = sleep_sample_10_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 2, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_11_0 = (ring 34.01,4.0,4.01,11.98,8.0,6.0,8.0,8.01,33.99,8.0,6.0,4.0,4.0,4.0,6.0,8.0,12.0,8.0,6.0,8.0,8.01,-1)
live_loop :loop_sample_11_0 do
	sleep_time = sleep_sample_11_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 3, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_11_1 = (ring 56.0,8.0,6.0,50.0,8.0,24.0,8.0,20.0,6.0,8.0,-1)
live_loop :loop_sample_11_1 do
	sleep_time = sleep_sample_11_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 3, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_12_0 = (ring 24.01,8.0,8.0,15.99,8.0,4.0,4.0,4.0,44.0,8.0,44.0,8.0,8.0,8.0,4.01,3.99,4.01,3.99,-1)
live_loop :loop_sample_12_0 do
	sleep_time = sleep_sample_12_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 4, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_13_0 = (ring 20.01,4.0,4.0,23.99,4.0,4.0,4.0,8.0,12.01,8.01,15.99,15.99,6.0,6.0,4.0,16.0,16.0,4.0,12.0,4.0,4.0,8.0,8.0,-1)
live_loop :loop_sample_13_0 do
	sleep_time = sleep_sample_13_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 5, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_13_1 = (ring 132.0,-1)
live_loop :loop_sample_13_1 do
	sleep_time = sleep_sample_13_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 5, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_14_0 = (ring 22.01,47.99,8.0,8.01,8.01,8.0,33.98,50.0,16.0,8.01,-1)
live_loop :loop_sample_14_0 do
	sleep_time = sleep_sample_14_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 6, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_14_1 = (ring 88.02,8.0,7.99,-1)
live_loop :loop_sample_14_1 do
	sleep_time = sleep_sample_14_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 6, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_15_0 = (ring 82.02,3.99,4.01,4.0,4.0,4.0,4.0,3.99,91.99,-1)
live_loop :loop_sample_15_0 do
	sleep_time = sleep_sample_15_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 7, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_15_1 = (ring 84.01,4.01,4.0,4.0,4.01,3.98,4.0,4.0,91.99,-1)
live_loop :loop_sample_15_1 do
	sleep_time = sleep_sample_15_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 7, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_2_0 = (ring 2.0,8.0,8.01,6.0,4.0,6.0,8.01,7.98,8.0,8.0,8.0,8.02,8.0,8.0,8.0,7.98,8.0,8.0,8.0,8.0,8.0,12.0,8.0,8.0,8.0,8.0,6.0,4.01,3.99,-1)
live_loop :loop_sample_2_0 do
	sleep_time = sleep_sample_2_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 8, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_2_1 = (ring 20.01,5.99,10.01,8.0,23.99,16.01,8.01,8.01,7.98,23.99,8.0,8.0,8.0,28.0,16.01,5.99,-1)
live_loop :loop_sample_2_1 do
	sleep_time = sleep_sample_2_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 8, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_3_0 = (ring 24.01,27.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,28.01,7.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,8.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,8.0,-1)
live_loop :loop_sample_3_0 do
	sleep_time = sleep_sample_3_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 9, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_3_1 = (ring 66.0,4.0,4.0,4.0,56.0,8.0,8.0,8.0,28.0,8.0,-1)
live_loop :loop_sample_3_1 do
	sleep_time = sleep_sample_3_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 9, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_4_0 = (ring 2.0,4.0,4.0,4.0,8.01,8.0,8.0,11.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,10.02,18.0,3.99,3.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.01,3.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,8.0,4.0,4.01,-1)
live_loop :loop_sample_4_0 do
	sleep_time = sleep_sample_4_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 10, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_4_1 = (ring 4.0,4.0,4.0,44.0,8.0,8.0,40.01,23.99,8.0,8.0,8.0,4.01,7.99,16.0,8.0,-1)
live_loop :loop_sample_4_1 do
	sleep_time = sleep_sample_4_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 10, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_5_0 = (ring 2.0,4.0,4.0,4.0,4.01,4.0,3.99,4.01,4.0,4.0,4.01,3.99,25.99,30.02,7.99,17.99,36.01,23.99,8.0,10.0,-1)
live_loop :loop_sample_5_0 do
	sleep_time = sleep_sample_5_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 11, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_5_1 = (ring 8.0,4.0,4.0,8.01,4.0,4.0,8.0,157.99,-1)
live_loop :loop_sample_5_1 do
	sleep_time = sleep_sample_5_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 11, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_6_0 = (ring 2.0,4.0,6.0,8.01,8.0,8.0,8.0,23.99,8.0,40.0,52.0,16.0,16.01,3.99,4.01,-1)
live_loop :loop_sample_6_0 do
	sleep_time = sleep_sample_6_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 12, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_6_1 = (ring 4.0,4.0,-1)
live_loop :loop_sample_6_1 do
	sleep_time = sleep_sample_6_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 12, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_7_0 = (ring 50.0,4.0,4.0,4.0,4.0,8.0,24.02,5.99,9.99,4.0,4.0,4.0,4.0,8.0,8.0,8.0,12.0,4.0,4.0,4.0,4.0,8.0,-1)
live_loop :loop_sample_7_0 do
	sleep_time = sleep_sample_7_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 13, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_7_1 = (ring 156.0,20.0,-1)
live_loop :loop_sample_7_1 do
	sleep_time = sleep_sample_7_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 13, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_8_0 = (ring 38.01,48.0,8.01,8.0,7.99,23.99,8.0,8.0,8.0,-1)
live_loop :loop_sample_8_0 do
	sleep_time = sleep_sample_8_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 14, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_8_1 = (ring 88.02,8.0,7.99,31.99,16.0,8.0,-1)
live_loop :loop_sample_8_1 do
	sleep_time = sleep_sample_8_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 14, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_9_0 = (ring 84.01,16.02,3.98,4.0,4.0,19.99,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.01,27.99,8.01,8.0,-1)
live_loop :loop_sample_9_0 do
	sleep_time = sleep_sample_9_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 15, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_9_1 = (ring 102.02,7.99,43.99,8.01,-1)
live_loop :loop_sample_9_1 do
	sleep_time = sleep_sample_9_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 15, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 2.02, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_0_0 = (ring 7.31,3.43,3.43,3.42,3.43,3.43,3.43,3.43,20.57,3.43,3.43,3.43,5.14,3.43,3.43,-1)
live_loop :loop_sample_0_0 do
	sleep_time = sleep_sample_0_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 16, start: 0.0, attack: 0.0, attack_level: 0.537, decay: 0.628, decay_level: 0.682, sustain: 1.114, sustain_level: 0.537, release: 0.0
	end
end
sleep_sample_0_1 = (ring 9.03,3.43,3.42,3.43,3.43,3.43,3.43,3.43,20.57,3.43,3.43,8.57,6.85,-1)
live_loop :loop_sample_0_1 do
	sleep_time = sleep_sample_0_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 16, start: 0.0, attack: 0.0, attack_level: 0.537, decay: 0.628, decay_level: 0.682, sustain: 1.114, sustain_level: 0.537, release: 0.0
	end
end
sleep_sample_1_0 = (ring 2.07,1.75,30.93,3.47,3.38,5.12,30.87,3.1,3.15,-1)
live_loop :loop_sample_1_0 do
	sleep_time = sleep_sample_1_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 17, start: 0, attack: 0, attack_level: 0.395, decay: 0, decay_level: 0.395, sustain: 1.741, sustain_level: 0.395, release: 0.0
	end
end
sleep_sample_1_1 = (ring 36.49,3.45,3.36,35.84,3.18,-1)
live_loop :loop_sample_1_1 do
	sleep_time = sleep_sample_1_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 17, start: 0, attack: 0, attack_level: 0.395, decay: 0, decay_level: 0.395, sustain: 1.741, sustain_level: 0.395, release: 0.0
	end
end
sleep_sample_2_0 = (ring 7.31,3.43,3.43,3.42,3.43,3.43,3.43,3.43,20.57,3.43,3.43,3.43,10.28,-1)
live_loop :loop_sample_2_0 do
	sleep_time = sleep_sample_2_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 18, start: 0.0, attack: 0.053, attack_level: 0.777, decay: 0.228, decay_level: 0.89, sustain: 1.436, sustain_level: 0.818, release: 0.024
	end
end
sleep_sample_2_1 = (ring 22.74,6.86,-1)
live_loop :loop_sample_2_1 do
	sleep_time = sleep_sample_2_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 18, start: 0.0, attack: 0.053, attack_level: 0.777, decay: 0.228, decay_level: 0.89, sustain: 1.436, sustain_level: 0.818, release: 0.024
	end
end
sleep_sample_3_0 = (ring 2.07,13.81,49.71,3.44,3.42,3.43,-1)
live_loop :loop_sample_3_0 do
	sleep_time = sleep_sample_3_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 19, start: 0.0, attack: 0.0, attack_level: 0.526, decay: 0.063, decay_level: 0.82, sustain: 1.624, sustain_level: 0.81, release: 0.055
	end
end
sleep_sample_3_1 = (ring 17.59,49.72,3.43,3.43,-1)
live_loop :loop_sample_3_1 do
	sleep_time = sleep_sample_3_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 19, start: 0.0, attack: 0.0, attack_level: 0.526, decay: 0.063, decay_level: 0.82, sustain: 1.624, sustain_level: 0.81, release: 0.055
	end
end
sleep_sample_4_0 = (ring 5.56,44.59,20.59,8.4,4.7,-1)
live_loop :loop_sample_4_0 do
	sleep_time = sleep_sample_4_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 20, start: 0.0, attack: 0.0, attack_level: 0.536, decay: 0.424, decay_level: 1.0, sustain: 1.311, sustain_level: 1.0, release: 0.006
	end
end
sleep_sample_5_0 = (ring 80.69,-1)
live_loop :loop_sample_5_0 do
	sleep_time = sleep_sample_5_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 21, start: 0.0, attack: 0.0, attack_level: 0.206, decay: 0.409, decay_level: 0.742, sustain: 1.267, sustain_level: 0.634, release: 0.066
	end
end
sleep_sample_6_0 = (ring 2.07,5.24,3.43,10.28,3.43,13.77,8.5,5.16,3.43,10.28,3.44,13.29,-1)
live_loop :loop_sample_6_0 do
	sleep_time = sleep_sample_6_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 22, start: 0.0, attack: 0.01, attack_level: 0.607, decay: 0.099, decay_level: 0.87, sustain: 1.501, sustain_level: 0.756, release: 0.132
	end
end
sleep_sample_6_1 = (ring 9.03,44.57,13.71,-1)
live_loop :loop_sample_6_1 do
	sleep_time = sleep_sample_6_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 22, start: 0.0, attack: 0.01, attack_level: 0.607, decay: 0.099, decay_level: 0.87, sustain: 1.501, sustain_level: 0.756, release: 0.132
	end
end
sleep_sample_7_0 = (ring 39.94,23.94,13.71,-1)
live_loop :loop_sample_7_0 do
	sleep_time = sleep_sample_7_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 23, start: 0.0, attack: 0.0, attack_level: 0.58, decay: 0.124, decay_level: 0.869, sustain: 1.615, sustain_level: 0.781, release: 0.002
	end
end
sleep_sample_8_0 = (ring 0.32,12.14,10.28,3.43,8.58,22.28,13.71,3.43,-1)
live_loop :loop_sample_8_0 do
	sleep_time = sleep_sample_8_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 24, start: 0.0, attack: 0.042, attack_level: 0.361, decay: 0.15, decay_level: 0.712, sustain: 1.549, sustain_level: 0.444, release: 0.0
	end
end
sleep_sample_8_1 = (ring 14.17,10.28,3.43,8.61,22.25,13.71,-1)
live_loop :loop_sample_8_1 do
	sleep_time = sleep_sample_8_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 24, start: 0.0, attack: 0.042, attack_level: 0.361, decay: 0.15, decay_level: 0.712, sustain: 1.549, sustain_level: 0.444, release: 0.0
	end
end
sleep_sample_9_0 = (ring 0.32,1.75,42.93,-1)
live_loop :loop_sample_9_0 do
	sleep_time = sleep_sample_9_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 25, start: 0.0, attack: 0.001, attack_level: 0.397, decay: 0.176, decay_level: 0.341, sustain: 1.565, sustain_level: 0.444, release: 0.0
	end
end
