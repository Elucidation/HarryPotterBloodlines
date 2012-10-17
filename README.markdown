While reading [Harry Potter and the Methods of Rationality](http://hpmor.com/) on [chapter 23](http://hpmor.com/chapter/23).
The idea is magic is a 1 or more gene in your dna, and that affects how it could be passed down to your children, and how magically inclined they could possible be.
So I went ahead and implemented a simple python version of it, when the dna length is >1 it's how Draco thinks of it, and when it's = 1, it's how Harry thinks of it.

Hooked up a little name generator to it, and an ancestry function to see a bit of your parent tree.

With DNA Length > 1, Like Draco thinks:

	Seed used: 43425264
	People per generation: 200, Total number of generations: 200
	Creating world... Done.
	World:: Generation 0 :: Population: 200, Wizards: 2, Squibs: 187, Muggles: 11
	       Arsherp Agsaw. Born in the year 0. She is a Squib. Her parents are Alpha and Omega DNA: ___MMM_M__/_MMM__M__M
	        Rawiy Ahouth. Born in the year 0. She is a Squib. Her parents are Alpha and Omega DNA: MMMM__MM__/M_MMM_MMM_
	        Oiyary Aktoo. Born in the year 0. He is a Squib. His parents are Alpha and Omega DNA: MM___M____/M_M_M_M_MM
		          											...
	       Awmawl Whuraw. Born in the year 0. She is a Squib. Her parents are Alpha and Omega DNA: ___M____MM/_MMMM__M_M
	          Idej Xepar. Born in the year 0. He is a Squib. His parents are Alpha and Omega DNA: MM__MMMM__/M___MM__MM
	       Arrarf Xoipoi. Born in the year 0. She is a Squib. Her parents are Alpha and Omega DNA: _MMM_MM___/MMMMMM__M_
	         Thuij Xouji. Born in the year 0. He is a Squib. His parents are Alpha and Omega DNA: __M_______/M_M_MMMM_M
	          Moshi Yimu. Born in the year 0. He is a Squib. His parents are Alpha and Omega DNA: MMM_____MM/_M__M__MMM
	         Awpxou Yudo. Born in the year 0. He is a Squib. His parents are Alpha and Omega DNA: ____MMM_M_/MMMMM_____

	Running world... Done.
	World:: Generation 199 :: Population: 200, Wizards: 12, Squibs: 185, Muggles: 3
	      Awngers Equoiv. Born in the year 187. She is a Squib. Her parents are Utxu Equoiv and Doouz Oubpoo DNA: MMMM_M_M_M/MM_____M_M
	      Chawlar Equoiv. Born in the year 196. She is a Squib. Her parents are Joisu Equoiv and Epesh Oubpoo DNA: MMM___MM__/M_M__M_MMM
		          											...
	       Xuawng Oubpoo. Born in the year 176. He is a Squib. His parents are Yochu Oithawp and Osoc Oubpoo DNA: MMM__M_M_M/__MM___MM_
	         Yuuz Oubpoo. Born in the year 197. He is a Wizard!. His parents are Iwhoong Oubpoo and Oothequ Ougker DNA: MMM_M_MMMM/MMMM__MMMM
	       Zooker Oubpoo. Born in the year 198. She is a Squib. Her parents are *Ernsaw Oubpoo* and Ukcha Hoen DNA: MMM__MMMM_/MM__M_MMM_
	       Oivooy Ougker. Born in the year 188. She is a Squib. Her parents are Oiquda Ougker and Mawit Ooshwhou DNA: _MMM_MMM_M/_MMM___MM_
	      Oothequ Ougker. Born in the year 192. She is a Squib. Her parents are Nawro Hoen and Oivooy Ougker DNA: MMM___MMMM/_MMM__MM_M

	All people in world dead/alive: 4180, People who lived beyond 40: 43
	Number of all wizards who ever existed: 137
	##########################
	Ancestry of *Oochiy Oithawp*, born 199. Current age 0. Female. Dad & Mum are Ihos Oithawp and *Uksher Oithawp*.
	###############
	#Patriarchy
	*Oochiy Oithawp* (B:199 D:---, Age 0), Magic level: 85%
	    ^ Ihos Oithawp (B:192 D:---, Age 7), Magic level: 50%
	      ^ Ngawcha Oithawp (B:188 D:---, Age 11), Magic level: 55%
	        ^ Fariv Oithawp (B:184 D:196, Age 12), Magic level: 55%
	          ^ Jiawc Oithawp (B:177 D:196, Age 19), Magic level: 55%
	            ^ Uquper Oithawp (B:168 D:191, Age 23), Magic level: 60%
	              ^ Jawerk Hoen (B:151 D:180, Age 29), Magic level: 65%
	                ^ Deawl Hoen (B:147 D:157, Age 10), Magic level: 55%
	                  ^ Abcou Hoen (B:147 D:152, Age 5), Magic level: 60%
	                    ^ Daroush Hoen (B:147 D:150, Age 3), Magic level: 45%
	                      ^ Ekerwh Hoen (B:134 D:160, Age 26), Magic level: 60%
	                        ^ Erwhbe Hoen (B:114 D:164, Age 50), Magic level: 60%
	                          ^ Zous Hoen (B:090 D:125, Age 35), Magic level: 45%
	                            ^ Shoucha Hoen (B:075 D:092, Age 17), Magic level: 30%
	                              ^ Inva Hoen (B:048 D:089, Age 41), Magic level: 30%
	                                ^ Erqungar Hoen (B:041 D:060, Age 19), Magic level: 50%
	                                  ^ Usuc Hoen (B:036 D:064, Age 28), Magic level: 50%
	                                    ^ Oipngu Hoen (B:015 D:053, Age 38), Magic level: 45%
	                                      ^ Yawse Ethux (B:013 D:034, Age 21), Magic level: 65%
	                                        ^ Sarjaw Ethux (B:012 D:018, Age 6), Magic level: 65%
	                                          ^ Foiark Ethux (B:000 D:017, Age 17), Magic level: 65%
	###############
	#Matriarchy
	*Oochiy Oithawp* (B:199 D:---, Age 0), Magic level: 85%
	    ^ *Uksher Oithawp* (B:193 D:---, Age 6), Magic level: 90%
	      ^ *Derow Oithawp* (B:183 D:199, Age 16), Magic level: 90%
	        ^ *Awzat Biyer* (B:182 D:185, Age 3), Magic level: 80%
	          ^ Noiouk Biyer (B:139 D:183, Age 44), Magic level: 65%
	            ^ Goubar Equoiv (B:138 D:143, Age 5), Magic level: 55%
	              ^ Darko Hoen (B:127 D:150, Age 23), Magic level: 55%
	                ^ Echchu Hoen (B:120 D:140, Age 20), Magic level: 55%
	                  ^ Awwart Narchi (B:094 D:145, Age 51), Magic level: 65%
	                    ^ Meroof Narchi (B:093 D:095, Age 2), Magic level: 40%
	                      ^ Zerouz Narchi (B:087 D:101, Age 14), Magic level: 45%
	                        ^ Awpov Equoiv (B:080 D:088, Age 8), Magic level: 65%
	                          ^ Oomoob Oithawp (B:080 D:092, Age 12), Magic level: 55%
	                            ^ Agec Oithawp (B:057 D:095, Age 38), Magic level: 45%
	                              ^ Oxor Oithawp (B:057 D:063, Age 6), Magic level: 65%
	                                ^ Erpquo Osnu (B:031 D:060, Age 29), Magic level: 55%
	                                  ^ Vewou Agsaw (B:031 D:041, Age 10), Magic level: 70%
	                                    ^ Ervoo Agsaw (B:027 D:037, Age 10), Magic level: 70%
	                                      ^ Awgza Ederj (B:024 D:031, Age 7), Magic level: 50%
	                                        ^ Erbwa Ederj (B:020 D:032, Age 12), Magic level: 50%
	                                          ^ Fawu Ayngu (B:000 D:029, Age 29), Magic level: 45%
	[Finished in 0.5s]

With DNA Length = 1, Like Harry thinks:

	Seed used: 5265233
	People per generation: 200, Total number of generations: 200
	Creating world... Done.
	World:: Generation 0 :: Population: 200, Wizards: 57, Squibs: 97, Muggles: 46
	         Ercon Afpaw. Born in the year 0. She is a Wizard!. Her parents are Alpha and Omega DNA: M/M
	       Ertiwh Agwhoo. Born in the year 0. He is a Wizard!. His parents are Alpha and Omega DNA: M/M
	        Thachu Alois. Born in the year 0. He is a Wizard!. His parents are Alpha and Omega DNA: M/M
	        											...
	         Ogawg Zerur. Born in the year 0. He is a Squib. His parents are Alpha and Omega DNA: _/M
	        Ogoth Zerzaw. Born in the year 0. She is a Wizard!. Her parents are Alpha and Omega DNA: M/M
	        Ighoo Zouyoo. Born in the year 0. She is a Squib. Her parents are Alpha and Omega DNA: _/M
	         Uyquoi Zumo. Born in the year 0. He is a Wizard!. His parents are Alpha and Omega DNA: M/M

	Running world... Done.
	World:: Generation 199 :: Population: 200, Wizards: 52, Squibs: 103, Muggles: 45
	         Ahlou Erwgo. Born in the year 167. She is a Wizard!. Her parents are *Ledo Erwgo* and *Oigvar Quopoo* DNA: M/M
	          Akse Erwgo. Born in the year 197. He is a Muggle. His parents are Urgu Erwgo and Gouw Quopoo DNA: _/_
	          											...
	          Utca Ruech. Born in the year 191. He is a Squib. His parents are Oquaws Ruech and Oozzoi Erwgo DNA: M/_
	        Warzoo Ruech. Born in the year 195. She is a Squib. Her parents are *Ewoud Ruech* and Joiung Quopoo DNA: M/_
	        Woawsh Ruech. Born in the year 198. She is a Squib. Her parents are Noas Ruech and *Ojzou Erwgo* DNA: _/M
	         Yiouy Ruech. Born in the year 199. He is a Wizard!. His parents are *Ewoud Ruech* and Joiung Quopoo DNA: M/M


	All people in world dead/alive: 4180, People who lived beyond 40: 53
	Number of all wizards who ever existed: 1057
	##########################
	Ancestry of *Oowhlo Quopoo*, born 199. Current age 0. Female. Dad & Mum are Chawawt Quopoo and *Arven Kearr*.
	###############
	#Patriarchy
	*Oowhlo Quopoo* (B:199 D:---, Age 0), Magic level: 100%
	    ^ Chawawt Quopoo (B:176 D:---, Age 23), Magic level: 50%
	      ^ Chuzar Quopoo (B:162 D:190, Age 28), Magic level: 50%
	        ^ Artoqu Quopoo (B:162 D:165, Age 3), Magic level: 50%
	          ^ Ikvoi Quopoo (B:152 D:163, Age 11), Magic level: 50%
	            ^ Oiloong Quopoo (B:131 D:153, Age 22), Magic level: 50%
	              ^ Arkjoi Quopoo (B:084 D:138, Age 54), Magic level: 0%
	                ^ Ikci Oowhoog (B:079 D:094, Age 15), Magic level: 0%
	                  ^ Queawx Oowhoog (B:076 D:085, Age 9), Magic level: 50%
	                    ^ Oijoig Oowhoog (B:052 D:091, Age 39), Magic level: 0%
	                      ^ Emoul Quoimer (B:046 D:071, Age 25), Magic level: 50%
	                        ^ Lerap Quoimer (B:042 D:048, Age 6), Magic level: 50%
	                          ^ Zawos Quoimer (B:041 D:044, Age 3), Magic level: 50%
	                            ^ Oirab Quoimer (B:039 D:054, Age 15), Magic level: 50%
	                              ^ *Zouic Quoimer* (B:034 D:048, Age 14), Magic level: 100%
	                                ^ *Ejshi Quoimer* (B:015 D:035, Age 20), Magic level: 100%
	                                  ^ *Ferngou Quoimer* (B:002 D:023, Age 21), Magic level: 100%
	                                    ^ *Terwo Kearr* (B:000 D:014, Age 14), Magic level: 100%
	###############
	#Matriarchy
	*Oowhlo Quopoo* (B:199 D:---, Age 0), Magic level: 100%
	    ^ *Arven Kearr* (B:186 D:---, Age 13), Magic level: 100%
	      ^ Tawuh Fushe (B:150 D:187, Age 37), Magic level: 50%
	        ^ Voopou Fushe (B:148 D:154, Age 6), Magic level: 0%
	          ^ Axri Fushe (B:097 D:152, Age 55), Magic level: 50%
	            ^ Arksaw Quoimer (B:085 D:115, Age 30), Magic level: 50%
	              ^ Erqusu Erwgo (B:082 D:085, Age 3), Magic level: 50%
	                ^ Arthlar Quopoo (B:060 D:096, Age 36), Magic level: 0%
	                  ^ Arquosh Quopoo (B:050 D:061, Age 11), Magic level: 0%
	                    ^ Sooeb Quoimer (B:032 D:053, Age 21), Magic level: 50%
	                      ^ *Ouwherw Tarpoi* (B:020 D:049, Age 29), Magic level: 100%
	                        ^ Wheawv Tarpoi (B:014 D:021, Age 7), Magic level: 50%
	                          ^ Ojwoo Tarpoi (B:000 D:015, Age 15), Magic level: 0%
	[Finished in 1.1s]