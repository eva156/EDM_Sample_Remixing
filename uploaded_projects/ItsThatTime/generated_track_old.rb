samps = 'C:\Users\uno4e\OneDrive\Documents\Cambridge II\project_updated\uploaded_projects\ItsThatTime\samples'
use_bpm 73.828125
set :max_time, 240.24997732426303
live_loop :start do
	sleep get[:max_time]
	cue 'start'
end
sleep_sample_0_0 = (ring 13.41,1.64,3.26,1.64,111.01,1.64,3.26,3.27,-1)
live_loop :loop_sample_0_0 do
	sleep_time = sleep_sample_0_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 0, start: 0.015, attack: 0.0, attack_level: 1.0, decay: 0.388, decay_level: 0.0, sustain: 1.235, sustain_level: 0.0, release: 0.0
	end
end
sleep_sample_0_1 = (ring 16.68,4.9,112.65,3.26,-1)
live_loop :loop_sample_0_1 do
	sleep_time = sleep_sample_0_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 0, start: 0.015, attack: 0.0, attack_level: 1.0, decay: 0.388, decay_level: 0.0, sustain: 1.235, sustain_level: 0.0, release: 0.0
	end
end
sleep_sample_1_0 = (ring 23.21,14.69,13.06,14.69,1.64,34.29,52.24,26.12,14.7,3.26,1.64,3.26,3.27,3.26,3.27,3.26,3.27,-1)
live_loop :loop_sample_1_0 do
	sleep_time = sleep_sample_1_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 1, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_1_1 = (ring 24.84,44.08,127.35,4.9,3.26,6.53,3.27,3.26,-1)
live_loop :loop_sample_1_1 do
	sleep_time = sleep_sample_1_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 1, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_10_0 = (ring 21.58,62.04,13.06,13.06,6.53,6.53,9.8,3.26,3.27,48.98,-1)
live_loop :loop_sample_10_0 do
	sleep_time = sleep_sample_10_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 2, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_10_1 = (ring 134.23,6.53,-1)
live_loop :loop_sample_10_1 do
	sleep_time = sleep_sample_10_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 2, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_11_0 = (ring 15.05,3.26,3.27,6.53,6.53,6.53,6.53,6.53,6.53,17.96,6.53,4.9,3.26,4.9,6.53,6.53,3.27,3.26,3.27,3.26,6.53,3.27,3.26,1.64,6.53,6.53,6.53,4.9,3.26,4.9,4.9,6.53,6.53,-1)
live_loop :loop_sample_11_0 do
	sleep_time = sleep_sample_11_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 3, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_11_1 = (ring 16.68,13.06,6.53,6.53,6.53,6.53,24.49,6.53,4.9,8.16,16.33,6.53,24.49,13.06,4.9,8.16,4.9,6.53,6.53,-1)
live_loop :loop_sample_11_1 do
	sleep_time = sleep_sample_11_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 3, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_12_0 = (ring 13.41,1.64,4.9,63.67,13.06,13.06,6.53,6.53,8.16,1.64,3.26,3.27,48.98,13.06,-1)
live_loop :loop_sample_12_0 do
	sleep_time = sleep_sample_12_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 4, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_12_1 = (ring 16.68,-1)
live_loop :loop_sample_12_1 do
	sleep_time = sleep_sample_12_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 4, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_13_0 = (ring 26.47,1.64,3.26,1.64,3.26,3.26,1.64,3.26,1.64,3.26,3.26,1.64,4.9,3.26,1.64,3.26,11.43,3.27,3.26,3.27,4.89,1.64,3.26,3.27,3.26,3.27,4.9,4.89,3.27,3.26,1.64,17.96,3.26,3.27,6.53,4.89,1.64,4.9,3.26,3.27,3.26,4.9,3.27,3.26,3.27,6.53,13.06,6.53,6.53,3.26,3.27,-1)
live_loop :loop_sample_13_0 do
	sleep_time = sleep_sample_13_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 5, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_13_1 = (ring 29.74,4.9,3.26,4.9,4.9,3.26,4.9,4.9,4.89,14.7,6.53,3.27,6.53,3.26,9.8,4.9,8.16,4.9,17.96,13.06,6.53,4.9,6.53,8.16,3.27,3.26,3.27,-1)
live_loop :loop_sample_13_1 do
	sleep_time = sleep_sample_13_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 5, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_14_0 = (ring 15.05,3.26,1.64,8.16,4.9,3.26,9.8,13.06,4.9,14.69,3.27,3.26,3.27,3.26,3.27,4.89,8.17,4.9,6.53,3.26,3.27,6.53,3.26,3.27,4.9,6.53,6.53,6.53,4.9,6.53,8.16,3.27,3.26,3.27,-1)
live_loop :loop_sample_14_0 do
	sleep_time = sleep_sample_14_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 6, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_14_1 = (ring 16.68,4.9,8.16,4.9,48.98,3.26,3.27,6.53,13.06,11.43,13.06,11.43,13.06,11.43,17.96,3.26,-1)
live_loop :loop_sample_14_1 do
	sleep_time = sleep_sample_14_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 6, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_15_0 = (ring 21.58,57.14,8.16,13.06,13.07,13.06,4.89,1.64,3.26,3.27,44.08,8.16,-1)
live_loop :loop_sample_15_0 do
	sleep_time = sleep_sample_15_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 7, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_15_1 = (ring 134.23,3.26,-1)
live_loop :loop_sample_15_1 do
	sleep_time = sleep_sample_15_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 7, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_16_0 = (ring 13.41,1.64,3.26,1.64,8.16,3.26,1.64,8.16,4.9,3.26,4.9,4.9,19.59,3.27,3.26,3.27,3.26,3.27,3.26,6.53,3.27,3.26,1.64,3.26,3.27,3.26,8.16,1.64,3.26,3.27,4.9,3.26,3.27,6.53,3.26,3.27,3.26,1.64,3.26,4.9,6.53,3.27,3.26,3.27,6.53,13.06,-1)
live_loop :loop_sample_16_0 do
	sleep_time = sleep_sample_16_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 8, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_16_1 = (ring 16.68,4.9,13.06,8.16,4.9,13.06,19.59,3.27,3.26,3.27,6.53,3.26,6.53,3.27,4.9,3.26,3.27,3.26,9.8,3.26,8.17,6.53,6.53,11.43,3.26,4.9,9.8,3.26,-1)
live_loop :loop_sample_16_1 do
	sleep_time = sleep_sample_16_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 8, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_17_0 = (ring 13.41,1.64,3.26,1.64,3.26,6.53,8.16,3.27,6.53,3.26,14.69,17.97,6.53,6.53,11.43,3.26,1.64,3.26,3.27,3.26,3.27,4.89,1.64,3.26,3.27,4.9,8.16,22.86,8.16,4.9,6.53,3.26,1.64,3.26,6.53,3.27,3.26,-1)
live_loop :loop_sample_17_0 do
	sleep_time = sleep_sample_17_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 9, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_17_1 = (ring 16.68,4.9,3.26,73.47,11.43,11.43,13.06,3.26,8.17,50.61,4.9,3.26,9.8,-1)
live_loop :loop_sample_17_1 do
	sleep_time = sleep_sample_17_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 9, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_18_0 = (ring 18.31,3.27,4.89,1.64,3.26,3.27,4.89,1.64,3.26,1.64,3.26,3.26,1.64,3.26,1.64,3.26,17.96,3.27,3.26,1.64,4.89,1.64,3.26,6.53,3.27,3.26,1.64,3.26,3.27,4.89,1.64,21.22,3.27,6.53,3.26,3.27,3.26,1.64,4.89,9.8,3.27,3.26,3.27,-1)
live_loop :loop_sample_18_0 do
	sleep_time = sleep_sample_18_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 10, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_18_1 = (ring 29.74,6.53,6.53,4.9,8.16,4.9,24.49,4.9,6.53,3.26,6.53,8.17,3.26,3.27,40.81,22.86,3.27,3.26,-1)
live_loop :loop_sample_18_1 do
	sleep_time = sleep_sample_18_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 10, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_2_0 = (ring 13.41,1.64,3.26,1.64,176.32,3.27,3.26,3.27,3.26,3.27,3.26,6.53,1.64,3.26,-1)
live_loop :loop_sample_2_0 do
	sleep_time = sleep_sample_2_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 11, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_2_1 = (ring 16.68,4.9,176.32,3.27,3.26,6.53,3.27,3.26,8.17,-1)
live_loop :loop_sample_2_1 do
	sleep_time = sleep_sample_2_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 11, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_3_0 = (ring 13.41,3.27,9.79,4.9,8.16,4.9,4.9,3.26,3.27,24.49,6.53,6.53,4.9,6.53,6.53,6.53,6.53,6.53,3.27,3.26,11.43,11.43,13.06,11.43,6.53,13.06,13.06,-1)
live_loop :loop_sample_3_0 do
	sleep_time = sleep_sample_3_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 12, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_3_1 = (ring 18.31,39.18,42.45,6.53,29.39,26.12,-1)
live_loop :loop_sample_3_1 do
	sleep_time = sleep_sample_3_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 12, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_4_0 = (ring 0.35,3.26,3.26,1.64,3.27,14.69,1.64,3.26,3.27,4.89,1.64,3.26,3.27,3.26,3.27,3.26,3.27,3.27,4.89,3.27,3.26,4.9,3.27,3.26,3.27,3.26,3.27,3.26,1.64,3.26,4.9,6.53,3.27,3.26,3.27,3.26,13.07,3.26,3.26,1.64,3.26,3.27,3.26,3.27,3.26,1.64,3.26,3.27,3.26,3.26,1.64,4.9,3.26,16.33,11.43,3.26,1.64,3.26,3.26,1.64,-1)
live_loop :loop_sample_4_0 do
	sleep_time = sleep_sample_4_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 13, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_4_1 = (ring 1.97,3.27,4.9,19.6,6.53,6.53,6.53,3.26,3.27,6.53,3.26,4.9,3.27,3.26,14.7,11.43,3.26,11.43,6.53,3.27,16.33,3.26,4.9,3.26,3.27,3.26,3.27,4.9,3.26,3.27,3.26,4.9,35.92,8.16,4.9,-1)
live_loop :loop_sample_4_1 do
	sleep_time = sleep_sample_4_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 13, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_5_0 = (ring 39.53,1.64,3.26,1.64,3.26,3.26,1.64,3.26,1.64,3.26,1.64,3.26,3.26,1.64,3.26,29.39,3.27,3.26,1.64,3.26,3.27,3.26,3.27,3.26,3.27,3.26,3.27,4.9,3.26,3.27,3.26,16.33,3.26,1.64,3.26,3.26,14.7,3.27,3.26,3.27,-1)
live_loop :loop_sample_5_0 do
	sleep_time = sleep_sample_5_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 14, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_5_1 = (ring 42.8,4.9,3.26,4.9,4.9,4.89,3.27,4.9,32.65,3.27,4.9,3.26,3.27,3.26,3.27,3.26,3.27,3.26,3.27,4.9,3.26,3.27,19.59,4.9,3.26,17.96,3.27,3.26,3.27,-1)
live_loop :loop_sample_5_1 do
	sleep_time = sleep_sample_5_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 14, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_6_0 = (ring 78.72,3.27,3.26,3.27,3.26,3.27,3.26,3.27,3.26,3.27,3.26,1.64,4.89,1.64,4.89,1.64,4.89,1.64,3.26,3.27,6.53,6.53,31.02,3.27,3.26,3.27,3.26,3.27,3.26,3.27,-1)
live_loop :loop_sample_6_0 do
	sleep_time = sleep_sample_6_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 15, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_6_1 = (ring 80.35,3.27,3.26,6.53,3.27,3.26,6.53,8.17,6.53,6.53,6.53,3.26,3.27,44.08,3.27,3.26,-1)
live_loop :loop_sample_6_1 do
	sleep_time = sleep_sample_6_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 15, start: 0.0, attack: 0.0, attack_level: 1.0, decay: 0.0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_7_0 = (ring 13.41,3.27,4.9,94.69,14.69,1.64,3.26,3.27,-1)
live_loop :loop_sample_7_0 do
	sleep_time = sleep_sample_7_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 16, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_7_1 = (ring 18.31,115.92,3.26,3.27,-1)
live_loop :loop_sample_7_1 do
	sleep_time = sleep_sample_7_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 16, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_8_0 = (ring 19.95,8.16,4.9,8.16,4.9,35.92,6.53,6.53,13.06,4.9,6.53,6.53,6.53,6.53,4.9,6.53,17.96,6.53,11.43,6.53,6.53,6.53,17.96,-1)
live_loop :loop_sample_8_0 do
	sleep_time = sleep_sample_8_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 17, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_8_1 = (ring 34.64,48.98,50.61,11.43,6.53,35.92,37.55,-1)
live_loop :loop_sample_8_1 do
	sleep_time = sleep_sample_8_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 17, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_9_0 = (ring 13.41,1.64,3.26,1.64,13.06,48.98,6.53,6.53,37.55,6.53,47.35,6.53,6.53,13.06,-1)
live_loop :loop_sample_9_0 do
	sleep_time = sleep_sample_9_0.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 18, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
sleep_sample_9_1 = (ring 16.68,4.9,112.65,-1)
live_loop :loop_sample_9_1 do
	sleep_time = sleep_sample_9_1.tick()
	if sleep_time ==-1
		sync 'start'
	else
		sleep sleep_time
		sample samps, 18, start: 0, attack: 0, attack_level: 1.0, decay: 0, decay_level: 1.0, sustain: 1.637, sustain_level: 1.0, release: 0.0
	end
end
