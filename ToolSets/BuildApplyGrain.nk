set cut_paste_input [stack 0]
version 10.0 v4
push $cut_paste_input
Group {
 name build_grain
 help "created a balanced grain plate using an analysis between a graind plate and a degrained plate"
 selected true
 xpos -1416
 addUserKnob {20 CopyGrain}
 addUserKnob {15 samplebox l region}
 samplebox {1.25999999 1.179999948 2046.5 1150.5}
 addUserKnob {22 bbox -STARTLINE T "tn = nuke.thisNode()\nsamplebox = tn\['samplebox']\n\nsamplebox.setX(0)\nsamplebox.setY(0)\nsamplebox.setR(tn.width())\nsamplebox.setT(tn.height())"}
 addUserKnob {68 sampleres l resolution M {1:1 1:4 1:9 1:16 "" ""}}
 sampleres 1:9
 addUserKnob {3 sstep l INVISIBLE t "this determines how many samples to take form the source\n\n1 samples every pixel\n2 samples every second pixel on every second row\netc.\n\nlower numbers yield an exponentially slower analysis, but a better resulting curve" +INVISIBLE}
 sstep {{sampleres+1}}
 addUserKnob {7 pointinterval l interval t "the space between points on the curve" R 0.001 0.2}
 pointinterval 0.2
 addUserKnob {22 ANALYZE l "SAMPLE AND UPDATE CURVE" T "from collections import defaultdict\nfrom math import floor\nimport threading  \nimport json\n\ntn = nuke.thisNode()\n\ngrained_node = nuke.toNode('grained')\ndegrain_node = nuke.toNode('degrained')\n\nlookup_table = nuke.toNode('ColorLookup0')\['lut']\nold_curve_store  = tn\['data']\nold_curve = json.loads(old_curve_store.getText()) if old_curve_store.value() else \{ 'r':\[] , 'g':\[] , 'b':\[]  \}\n\ninterval = tn\['pointinterval'].value()\nexponent = 0.5\n\nx_bounds = \[  tn\['samplebox'].x() , tn\['samplebox'].r()  ]\ny_bounds = \[  tn\['samplebox'].y() , tn\['samplebox'].t()  ]\nstep = int(tn\['sstep'].value())\n\nresponse_samples = \{ 'r' : \[], 'g' : \[], 'b' : \[] \}\n\n#a unique bucket mapping for a range of samples\ndef quantized_bucket(value):\n  return int(floor(value**exponent/interval)) if value >0 else -int(floor((-value)**exponent/interval))\n\ndef generatecurve():\n  #sample the images\n  t = nuke.ProgressTask('Sampling...') \n  for x in xrange( int(x_bounds\[0]) , int(x_bounds\[1]) , step ):\n\n    if t.isCancelled():\n      return\n    t.setProgress(int(x/int(x_bounds\[1])*100))\n\n    for y in xrange( int(y_bounds\[0]) , int(y_bounds\[1]) ,step ):\n      for c in \['r','g','b']:\n       gs = grained_node.sample(c,x,y)\n       ds = degrain_node.sample(c,x,y)\n       response_samples\[c].append( \[ds , abs(gs-ds)] ) \n\n  #average the multiplier for each bucket\n  #put the curves in the color lookup\n  rc_index = \{ 'r' : 1, 'g' : 2, 'b' : 3 \}\n  newcurve = \{ 'r':\[] , 'g':\[] , 'b':\[]  \}\n  for c in \['r','g','b']:\n\n    t.setMessage('Generating ' + c + ' Curve')\n    t.setProgress(0)\n\n    #filter samples into buckets with weight 1\n    buckets = defaultdict(list)\n    \[ buckets\[quantized_bucket(l)].append(\[l,g,1]) for l, g in response_samples\[c] ]\n    #and put old curve values in the buckets too\n    \[ buckets\[quantized_bucket(l)].append(\[l,g,w]) for l,g,w in old_curve\[c] ]\n\n    #average samples and combine with old curves to create points \n    for k,b in buckets.items():\n      if t.isCancelled():\n        return\n      t.setProgress(int(k/len(buckets)*100))\n\n      #find the weighted mean of the samples\n      sum_x , sum_y , tot_weight = \[ sum(z) for z in zip(*\[\[l*w,g*w,w] for l,g,w in b]) ]\n      av_x = sum_x/tot_weight\n      av_y = sum_y/tot_weight\n      \n      #store new\n      newcurve\[c].append(\[av_x, av_y, tot_weight])\n\n    #copy the new data into the lookup curve\n    lookup_table.clearAnimated(rc_index\[c])\n    for k,v,w in newcurve\[c]:\n      lookup_table.setValueAt( v ,k , rc_index\[c] )\n    \n  #store the new curves as a string for next time\n  old_curve_store.setValue( json.dumps(newcurve) )\n  print json.dumps(newcurve)\n  \n  #a hack to force Catm-Rum\n  lookup_table.fromScript(lookup_table.toScript().replace('curve x','curve R x'))\n  del t\n    \n\n#threading.Thread(target=generatecurve).start()\ngeneratecurve()" +STARTLINE}
 addUserKnob {22 Reset -STARTLINE T "lookup_table = nuke.toNode('ColorLookup0')\['lut']\nsamples = nuke.thisNode()\['data'].setValue('')\nfor i in \[1,2,3]:\n lookup_table.clearAnimated(i)"}
 addUserKnob {1 data l INVISIBLE +INVISIBLE}
 data "\{\"r\": \[\[0.03822272430313589, 0.002042396890992487, 2870], \[0.10377744442360474, 0.0034351565075606523, 161711], \[0.21671061403098407, 0.00499861386909569, 63460], \[0.47471723543797245, 0.0075859453159737664, 11245], \[0.7935291096269714, 0.010722978136629452, 5643], \[1.2017366461222394, 0.014734833437660503, 3894], \[1.6720007884174313, 0.01627114392201835, 2725], \[2.2349032633380244, 0.019440290749744113, 1954], \[2.888158096034595, 0.022291377692558748, 1532], \[3.6072412634408604, 0.024892193100358423, 1395], \[4.429680971448468, 0.025186063718662954, 1795], \[5.28594486297123, 0.027099609375, 2016], \[6.06297959297153, 0.03001278914590747, 562], \[7.253186677631579, 0.03119860197368421, 76], \[8.3779296875, 0.029622395833333332, 36], \[9.383680555555555, 0.05642361111111111, 9], \[11.053819444444445, 0.025173611111111112, 9], \[12.271484375, 0.021484375, 4], \[13.892578125, 0.001953125, 8], \[15.359375, 0.010416666666666666, 3], \[16.7125, 0.009375, 5], \[18.4375, 0.00390625, 4], \[20.1015625, 0.005208333333333333, 6], \[22.6015625, 0.0, 2], \[23.875, 0.003125, 5], \[26.125, 0.0, 5], \[27.415625, 0.0, 5], \[30.578125, 0.0, 2], \[32.6640625, 0.0, 4], \[35.90625, 0.0, 1], \[37.98385663507109, 0.002517772511848341, 211], \[39.34375, 0.0, 9]], \"b\": \[\[0.03419536069476464, 0.002032256387340235, 9868], \[0.09104670556145632, 0.003583332817663109, 195611], \[0.22227338302160612, 0.005919011794607789, 27498], \[0.47903155007982273, 0.009358599855842547, 7869], \[0.8034458393193145, 0.01398812550854353, 4916], \[1.19294612649156, 0.01663637882894354, 3436], \[1.680969772561484, 0.02015691759587328, 2399], \[2.237812953712666, 0.02321172393528761, 1808], \[2.8757480913561078, 0.026960942891649412, 1449], \[3.605507718974461, 0.031276498902633676, 1253], \[4.426941609977324, 0.03235278486394558, 1323], \[5.315137353198401, 0.03346959332833583, 2001], \[6.080850490645634, 0.038202723771093176, 1363], \[7.033563410194175, 0.04547178398058253, 103], \[8.3765869140625, 0.0374755859375, 32], \[9.2234375, 0.040625, 5], \[11.159598214285714, 0.008928571428571428, 7], \[12.174479166666666, 0.0078125, 6], \[13.8857421875, 0.0107421875, 8], \[14.978515625, 0.00390625, 4], \[16.203125, 0.0, 2], \[18.253125, 0.00625, 5], \[20.54375, 0.0, 5], \[22.01875, 0.003125, 5], \[23.614583333333332, 0.0, 3], \[26.28125, 0.0125, 5], \[28.755208333333332, 0.0, 3], \[30.46875, 0.0, 1], \[33.25, 0.0, 3], \[35.873310810810814, 0.002533783783783784, 37], \[36.32125, 0.0026785714285714286, 175], \[38.645833333333336, 0.0, 3]], \"g\": \[\[0.03551461430614536, 0.0015874399061411616, 8183], \[0.10331849441810895, 0.0026914212596908915, 154978], \[0.21545649090640304, 0.0035098534953449, 64526], \[0.4745505398525281, 0.005215897120786517, 11125], \[0.7970244409699307, 0.007346453632857615, 6061], \[1.1999016989906044, 0.010158308270378365, 3938], \[1.6787389392921146, 0.012534691109119872, 2511], \[2.2380720964566927, 0.014938586778215223, 1905], \[2.88553823397853, 0.017246462264150945, 1537], \[3.5986206144379134, 0.019978990631888318, 1361], \[4.441644613947696, 0.023484929561021172, 1606], \[5.301896404109589, 0.028294092465753425, 1825], \[6.095599434290688, 0.027578328981723237, 1149], \[7.099469866071429, 0.02659970238095238, 168], \[8.34415064102564, 0.024839743589743588, 39], \[9.458333333333334, 0.0234375, 18], \[10.775, 0.0109375, 5], \[12.41015625, 0.010416666666666666, 6], \[13.653125, 0.003125, 5], \[14.966796875, 0.0078125, 4], \[16.80078125, 0.00390625, 8], \[18.7421875, 0.0, 4], \[20.80078125, 0.00390625, 4], \[22.28125, 0.0, 3], \[24.32421875, 0.0, 4], \[25.756696428571427, 0.0, 7], \[28.7109375, 0.0, 2], \[30.70703125, 0.0006510416666666666, 24], \[32.693552927927925, 0.0019707207207207205, 111], \[34.24789325842696, 0.0024578651685393258, 89]]\}"
 addUserKnob {6 exponent_panelDropped l "panel dropped state" -STARTLINE +HIDDEN}
 addUserKnob {41 lut l "" +STARTLINE T ColorLookup0.lut}
}
 Input {
  inputs 0
  name scan_denoise
  xpos 177
  ypos 968
  number 1
 }
 NoOp {
  name degrained
  xpos 177
  ypos 1016
 }
 Dot {
  name Dot11
  xpos 211
  ypos 1162
 }
set Nf87185f0 [stack 0]
 Input {
  inputs 0
  name scan_noise
  xpos 306
  ypos 969
 }
 NoOp {
  name grained
  xpos 306
  ypos 1013
 }
 Dot {
  name Dot2
  xpos 340
  ypos 1091
 }
 Dot {
  name Dot12
  xpos 642
  ypos 1091
 }
 Merge2 {
  inputs 2
  operation from
  name Merge23
  xpos 608
  ypos 1158
 }
push $Nf87185f0
 Dot {
  name Dot13
  xpos 211
  ypos 1241
 }
 ColorLookup {
  lut {master {}
    red {curve R x0.03822272271 0.002042396891 x0.1037774459 0.003435156508 x0.2167106122 0.004998613869 x0.4747172296 0.007585945316 x0.7935290933 0.01072297814 x1.201736689 0.01473483344 x1.672000766 0.01627114392 x2.234903336 0.01944029075 x2.888158083 0.02229137769 x3.607241154 0.0248921931 x4.429680824 0.02518606372 x5.285944939 0.02709960938 x6.062979698 0.03001278915 x7.253186703 0.03119860197 x8.377929688 0.03159442917 x9.383680344 0.03175091743 x11.05381966 0.0278388001 x12.27148438 0.021484375 x13.89257812 0.01438112371 x15.359375 0.01041666667 x16.71249962 0.009375 x18.4375 0.00390625 x20.1015625 0.005208333333 x23.875 0.003125 x37.9838562 0.002517772512}
    green {curve R x0.03551461548 0.001587439906 x0.1033184975 0.00269142126 x0.2154564857 0.003509853495 x0.4745505452 0.005215897121 x0.7970244288 0.007346453633 x1.1999017 0.01015830827 x1.678738952 0.01253469111 x2.238072157 0.01493858678 x2.88553834 0.01724646226 x3.598620653 0.01997899063 x4.441644669 0.02348492956 x5.301896572 0.02829409247 x6.095599651 0.02757832898 x7.099469662 0.02659970238 x8.344150543 0.02483974359 x9.458333015 0.0234375 x10.77499962 0.0156329982 x12.41015625 0.008434705436 x13.65312481 0.007339313626 x14.96679688 0.006087433547 x16.80078125 0.00390625 x20.80078125 0.00390625 x32.69355392 0.001970720721 x34.24789429 0.002457865169}
    blue {curve R x0.0341953598 0.002032256387 x0.09104670584 0.003583332818 x0.2222733796 0.005919011795 x0.4790315628 0.009358599856 x0.803445816 0.01398812551 x1.192946076 0.01663637883 x1.680969715 0.0201569176 x2.237812996 0.02321172394 x2.875748158 0.02696094289 x3.605507612 0.0312764989 x4.426941395 0.03235278486 x5.315137386 0.03346959333 x6.080850601 0.03820272377 x7.033563614 0.03926217929 x8.376586914 0.03973163292 x9.223437309 0.03613248467 x11.15959835 0.01234681904 x12.17447948 0.0078125 x13.88574219 0.005305014551 x14.97851562 0.005305014551 x18.25312424 0.003740165383 x22.01874924 0.003740165383 x26.28125 0.003114227206 x35.87331009 0.002533783784 x36.32125092 0.002678571429}
    alpha {}}
  name ColorLookup0
  xpos 378
  ypos 1237
 }
 MergeExpression {
  inputs 2
  expr0 Ar/Br
  expr1 Ag/Bg
  expr2 Ab/Bb
  channel3 {none none none -rgba.alpha}
  expr3 Aa/Ba
  name Divide1
  xpos 608
  ypos 1237
 }
 Output {
  name Output1
  xpos 608
  ypos 1336
 }
end_group
push $cut_paste_input
Group {
 name apply_grain
 help "a solution that requires less manual matching of grain than other solutions (achieved by sampling a source plate to get an approximation of a noise response).\nadds grain to a source by comparing a denoised plate \nto a noisy plate (the original).\n\nHow to use:\nANALYSIS\nfirst the noise response curve must be calculated, plug in a plate and a degrained version of the same plate and hit ANALYSE GRAIN RESPONSE. This should give you a good starting point, modify the curve as needed, smoothing it out if noise is present. \nSet the output to grain, the result should be a uniform brightness grain pattern, though some details from the plate may still be present due to an imperfect degrain.\n\nMOTTLING\nThe details still present are replaced by taking small patches from another area in the frame (defined by the mottling samplebox). Mottling is activated by activating the mask channel.\n\nExtra:\nif you have your own grain plate that you would like to use instead, this can be applied by first getting a noise response curve in the standard way, then pluggin the noise plate to the scan denoise input, and a constant into the scan noise channel.\n"
 selected true
 xpos -1416
 ypos 107
 addUserKnob {20 ApplyGrain}
 addUserKnob {1 data l INVISIBLE +INVISIBLE}
 data "\{\"r\": \[\[0.03822272430313589, 0.002042396890992487, 2870], \[0.10377744442360474, 0.0034351565075606523, 161711], \[0.21671061403098407, 0.00499861386909569, 63460], \[0.47471723543797245, 0.0075859453159737664, 11245], \[0.7935291096269714, 0.010722978136629452, 5643], \[1.2017366461222394, 0.014734833437660503, 3894], \[1.6720007884174313, 0.01627114392201835, 2725], \[2.2349032633380244, 0.019440290749744113, 1954], \[2.888158096034595, 0.022291377692558748, 1532], \[3.6072412634408604, 0.024892193100358423, 1395], \[4.429680971448468, 0.025186063718662954, 1795], \[5.28594486297123, 0.027099609375, 2016], \[6.06297959297153, 0.03001278914590747, 562], \[7.253186677631579, 0.03119860197368421, 76], \[8.3779296875, 0.029622395833333332, 36], \[9.383680555555555, 0.05642361111111111, 9], \[11.053819444444445, 0.025173611111111112, 9], \[12.271484375, 0.021484375, 4], \[13.892578125, 0.001953125, 8], \[15.359375, 0.010416666666666666, 3], \[16.7125, 0.009375, 5], \[18.4375, 0.00390625, 4], \[20.1015625, 0.005208333333333333, 6], \[22.6015625, 0.0, 2], \[23.875, 0.003125, 5], \[26.125, 0.0, 5], \[27.415625, 0.0, 5], \[30.578125, 0.0, 2], \[32.6640625, 0.0, 4], \[35.90625, 0.0, 1], \[37.98385663507109, 0.002517772511848341, 211], \[39.34375, 0.0, 9]], \"b\": \[\[0.03419536069476464, 0.002032256387340235, 9868], \[0.09104670556145632, 0.003583332817663109, 195611], \[0.22227338302160612, 0.005919011794607789, 27498], \[0.47903155007982273, 0.009358599855842547, 7869], \[0.8034458393193145, 0.01398812550854353, 4916], \[1.19294612649156, 0.01663637882894354, 3436], \[1.680969772561484, 0.02015691759587328, 2399], \[2.237812953712666, 0.02321172393528761, 1808], \[2.8757480913561078, 0.026960942891649412, 1449], \[3.605507718974461, 0.031276498902633676, 1253], \[4.426941609977324, 0.03235278486394558, 1323], \[5.315137353198401, 0.03346959332833583, 2001], \[6.080850490645634, 0.038202723771093176, 1363], \[7.033563410194175, 0.04547178398058253, 103], \[8.3765869140625, 0.0374755859375, 32], \[9.2234375, 0.040625, 5], \[11.159598214285714, 0.008928571428571428, 7], \[12.174479166666666, 0.0078125, 6], \[13.8857421875, 0.0107421875, 8], \[14.978515625, 0.00390625, 4], \[16.203125, 0.0, 2], \[18.253125, 0.00625, 5], \[20.54375, 0.0, 5], \[22.01875, 0.003125, 5], \[23.614583333333332, 0.0, 3], \[26.28125, 0.0125, 5], \[28.755208333333332, 0.0, 3], \[30.46875, 0.0, 1], \[33.25, 0.0, 3], \[35.873310810810814, 0.002533783783783784, 37], \[36.32125, 0.0026785714285714286, 175], \[38.645833333333336, 0.0, 3]], \"g\": \[\[0.03551461430614536, 0.0015874399061411616, 8183], \[0.10331849441810895, 0.0026914212596908915, 154978], \[0.21545649090640304, 0.0035098534953449, 64526], \[0.4745505398525281, 0.005215897120786517, 11125], \[0.7970244409699307, 0.007346453632857615, 6061], \[1.1999016989906044, 0.010158308270378365, 3938], \[1.6787389392921146, 0.012534691109119872, 2511], \[2.2380720964566927, 0.014938586778215223, 1905], \[2.88553823397853, 0.017246462264150945, 1537], \[3.5986206144379134, 0.019978990631888318, 1361], \[4.441644613947696, 0.023484929561021172, 1606], \[5.301896404109589, 0.028294092465753425, 1825], \[6.095599434290688, 0.027578328981723237, 1149], \[7.099469866071429, 0.02659970238095238, 168], \[8.34415064102564, 0.024839743589743588, 39], \[9.458333333333334, 0.0234375, 18], \[10.775, 0.0109375, 5], \[12.41015625, 0.010416666666666666, 6], \[13.653125, 0.003125, 5], \[14.966796875, 0.0078125, 4], \[16.80078125, 0.00390625, 8], \[18.7421875, 0.0, 4], \[20.80078125, 0.00390625, 4], \[22.28125, 0.0, 3], \[24.32421875, 0.0, 4], \[25.756696428571427, 0.0, 7], \[28.7109375, 0.0, 2], \[30.70703125, 0.0006510416666666666, 24], \[32.693552927927925, 0.0019707207207207205, 111], \[34.24789325842696, 0.0024578651685393258, 89]]\}"
 addUserKnob {6 exponent_panelDropped l "panel dropped state" -STARTLINE +HIDDEN}
 addUserKnob {41 lut l "" +STARTLINE T ColorLookup0.lut}
 addUserKnob {26 ""}
 addUserKnob {6 ispremult l "source is premultiplied" +STARTLINE}
 ispremult true
 addUserKnob {6 cancelinterference l "cancel interference" +STARTLINE}
 addUserKnob {41 maskChannelMask l mask T Dissolve2.maskChannelMask}
 addUserKnob {4 blendlevels l blend t "This is only important and used if using an alpha matte\nThe correct level of output grain needed to give a consistent result can be calculated properly if given the background that this comp uses.\n\nIf that's too hard to get, then you can use the bad guess option, which will only work well if the luminance doesnt change too much from your new content to the bg" -STARTLINE M {"BG input" "Bad Guess" "" "" "" ""}}
}
 Input {
  inputs 0
  name SOURCE
  xpos 23
  ypos 1427
 }
 Dot {
  name Dot8
  xpos 57
  ypos 1583
 }
set N98542ca0 [stack 0]
 Dot {
  name Dot3
  xpos 120
  ypos 1583
 }
set N18ee8580 [stack 0]
push $N18ee8580
 Shuffle {
  alpha white
  name Shuffle3
  xpos 186
  ypos 1579
 }
push $N18ee8580
 Shuffle {
  alpha black
  name Shuffle4
  xpos 86
  ypos 1635
 }
 Dissolve {
  inputs 2+1
  which 1
  name Dissolve2
  xpos 186
  ypos 1629
 }
set Ncdaa94e0 [stack 0]
 Dot {
  name Dot19
  xpos 220
  ypos 1783
 }
 Dot {
  name Dot9
  xpos 220
  ypos 2041
 }
set Nde39cfa0 [stack 0]
 Dot {
  name Dot18
  xpos 220
  ypos 2067
 }
push $N98542ca0
 Dot {
  name Dot21
  xpos 57
  ypos 1941
 }
set N16b99e0 [stack 0]
 Unpremult {
  name Unpremult1
  xpos 101
  ypos 1937
  disable {{!parent.ispremult}}
 }
 ColorLookup {
  lut {master {}
    red {curve R x0.03822272271 0.002042396891 x0.1037774459 0.003435156508 x0.2167106122 0.004998613869 x0.4747172296 0.007585945316 x0.7935290933 0.01072297814 x1.201736689 0.01473483344 x1.672000766 0.01627114392 x2.234903336 0.01944029075 x2.888158083 0.02229137769 x3.607241154 0.0248921931 x4.429680824 0.02518606372 x5.285944939 0.02709960938 x6.062979698 0.03001278915 x7.253186703 0.03119860197 x8.377929688 0.03159442917 x9.383680344 0.03175091743 x11.05381966 0.0278388001 x12.27148438 0.021484375 x13.89257812 0.01438112371 x15.359375 0.01041666667 x16.71249962 0.009375 x18.4375 0.00390625 x20.1015625 0.005208333333 x23.875 0.003125 x37.9838562 0.002517772512}
    green {curve R x0.03551461548 0.001587439906 x0.1033184975 0.00269142126 x0.2154564857 0.003509853495 x0.4745505452 0.005215897121 x0.7970244288 0.007346453633 x1.1999017 0.01015830827 x1.678738952 0.01253469111 x2.238072157 0.01493858678 x2.88553834 0.01724646226 x3.598620653 0.01997899063 x4.441644669 0.02348492956 x5.301896572 0.02829409247 x6.095599651 0.02757832898 x7.099469662 0.02659970238 x8.344150543 0.02483974359 x9.458333015 0.0234375 x10.77499962 0.0156329982 x12.41015625 0.008434705436 x13.65312481 0.007339313626 x14.96679688 0.006087433547 x16.80078125 0.00390625 x20.80078125 0.00390625 x32.69355392 0.001970720721 x34.24789429 0.002457865169}
    blue {curve R x0.0341953598 0.002032256387 x0.09104670584 0.003583332818 x0.2222733796 0.005919011795 x0.4790315628 0.009358599856 x0.803445816 0.01398812551 x1.192946076 0.01663637883 x1.680969715 0.0201569176 x2.237812996 0.02321172394 x2.875748158 0.02696094289 x3.605507612 0.0312764989 x4.426941395 0.03235278486 x5.315137386 0.03346959333 x6.080850601 0.03820272377 x7.033563614 0.03926217929 x8.376586914 0.03973163292 x9.223437309 0.03613248467 x11.15959835 0.01234681904 x12.17447948 0.0078125 x13.88574219 0.005305014551 x14.97851562 0.005305014551 x18.25312424 0.003740165383 x22.01874924 0.003740165383 x26.28125 0.003114227206 x35.87331009 0.002533783784 x36.32125092 0.002678571429}
    alpha {}}
  name ColorLookup0
  xpos 409
  ypos 1937
 }
 set Cd42ffe10 [stack 0]
set Nd42ffe10 [stack 0]
 Merge2 {
  inputs 2
  operation mask
  name Merge3
  xpos 531
  ypos 2063
 }
push $Nde39cfa0
 Input {
  inputs 0
  name BG
  xpos -118
  ypos 1429
  number 2
 }
 Dot {
  name Dot17
  xpos -84
  ypos 2015
 }
clone $Cd42ffe10 {
  xpos 310
  ypos 2011
  selected false
 }
 Merge2 {
  inputs 2
  operation stencil
  name Merge7
  xpos 310
  ypos 2037
 }
 Dot {
  name Dot10
  label "\npsuedo bg grain level"
  xpos 344
  ypos 2085
 }
 Dot {
  name Dot7
  xpos 344
  ypos 2120
 }
push $Nd42ffe10
 Merge2 {
  inputs 2
  operation from
  name Merge4
  xpos 409
  ypos 2116
 }
 Switch {
  inputs 2
  which {{parent.blendlevels}}
  name Switch2
  label "level\nto apply"
  xpos 531
  ypos 2104
 }
push $Ncdaa94e0
 Invert {
  name Invert1
  xpos 372
  ypos 1773
 }
 Input {
  inputs 0
  name grain
  xpos 608
  ypos 1430
  number 1
 }
 Grade {
  inputs 1+1
  multiply 2.546479089
  black_clamp false
  name Grade3
  label "cancel\ninterference\n8/pi"
  xpos 608
  ypos 1761
  disable {{!parent.cancelinterference}}
 }
 Dot {
  name Dot15
  tile_color 0x7aa9ff00
  xpos 642
  ypos 1975
 }
 MergeExpression {
  inputs 2
  expr0 Ar*Br
  expr1 Ag*Bg
  expr2 Ab*Bb
  channel3 {none none none -rgba.alpha}
  expr3 Aa/Ba
  name Multiply1
  xpos 608
  ypos 2215
 }
push $N16b99e0
 Dot {
  name Dot5
  xpos 57
  ypos 2355
 }
 Unpremult {
  name Unpremult2
  xpos 112
  ypos 2351
  disable {{!parent.ispremult}}
 }
 Merge2 {
  inputs 2
  operation plus
  output {rgba.red rgba.green rgba.blue -rgba.alpha}
  name Merge2
  xpos 608
  ypos 2351
 }
 Premult {
  name Premult1
  xpos 608
  ypos 2377
  disable {{!parent.ispremult}}
 }
 Output {
  name Output1
  xpos 608
  ypos 2521
 }
end_group
