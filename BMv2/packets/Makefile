
PCAP_DIR 	= 	pcap
LOG_DIR 	= 	log
P4SRC_DIR	=	p4src	 
RESULT_DIR  = /home/mncgpu4/INI_schemes/TINIEE/temp_result

ifndef P4SRC_FILE

P4_EE_1 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first.p4
P4_EE_2 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive.p4
P4_EE_3 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive.p4
No_EE_1 = /home/mncgpu4/INI_schemes/TINIEE/p4src/noee_adaptive_1.p4
No_EE_2 = /home/mncgpu4/INI_schemes/TINIEE/p4src/noee_adaptive_2.p4
No_EE_3 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive.p4
P4_NF = /home/mncgpu4/INI_schemes/TINIEE/p4src/normal_forwarding.p4



P4_EE_1_55 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_55.p4
P4_EE_2_55 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_55.p4
P4_EE_3_55 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_55.p4

P4_EE_1_60 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_60.p4
P4_EE_2_60 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_60.p4
P4_EE_3_60 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_60.p4

P4_EE_1_65 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_65.p4
P4_EE_2_65 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_65.p4
P4_EE_3_65 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_65.p4

P4_EE_1_70 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_70.p4
P4_EE_2_70 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_70.p4
P4_EE_3_70 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_70.p4

P4_EE_1_75 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_75.p4
P4_EE_2_75 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_75.p4
P4_EE_3_75 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_75.p4

P4_EE_1_80 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_80.p4
P4_EE_2_80 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_80.p4
P4_EE_3_80 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_80.p4

P4_EE_1_85 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_85.p4
P4_EE_2_85 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_85.p4
P4_EE_3_85 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_85.p4

P4_EE_1_90 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_90.p4
P4_EE_2_90 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_90.p4
P4_EE_3_90 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_90.p4

P4_EE_1_95 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_first_95.p4
P4_EE_2_95 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_95.p4
P4_EE_3_95 = /home/mncgpu4/INI_schemes/TINIEE/p4src/ee_adaptive_95.p4
endif

all: run

 
ITA_TINIEE_55:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_55} --p4_ee_2 ${P4_EE_2_55} --p4_ee_3 ${P4_EE_2_55} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.55

ITA_DINC_55:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_55} --p4_ee_2 ${P4_EE_2_55} --p4_ee_3 ${P4_EE_2_55} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.55

ITA_TINIEE_60:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_60} --p4_ee_2 ${P4_EE_2_60} --p4_ee_3 ${P4_EE_2_60} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.60

ITA_DINC_60:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_60} --p4_ee_2 ${P4_EE_2_60} --p4_ee_3 ${P4_EE_2_60} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.60

ITA_DINC_65:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_65} --p4_ee_2 ${P4_EE_2_65} --p4_ee_3 ${P4_EE_2_65} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.65

ITA_TINIEE_65:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_65} --p4_ee_2 ${P4_EE_2_65} --p4_ee_3 ${P4_EE_2_65} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.65
ITA_DINC_70:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_70} --p4_ee_2 ${P4_EE_2_70} --p4_ee_3 ${P4_EE_2_70} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.70

ITA_TINIEE_70:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_70} --p4_ee_2 ${P4_EE_2_70} --p4_ee_3 ${P4_EE_2_70} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.70
ITA_DINC_75:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_75} --p4_ee_2 ${P4_EE_2_75} --p4_ee_3 ${P4_EE_2_75} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.75

ITA_TINIEE_75:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_75} --p4_ee_2 ${P4_EE_2_75} --p4_ee_3 ${P4_EE_2_75} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.75

ITA_DINC_80:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_80} --p4_ee_2 ${P4_EE_2_80} --p4_ee_3 ${P4_EE_2_80} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.80

ITA_TINIEE_80:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_80} --p4_ee_2 ${P4_EE_2_80} --p4_ee_3 ${P4_EE_2_80} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.80

ITA_DINC_85:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_85} --p4_ee_2 ${P4_EE_2_85} --p4_ee_3 ${P4_EE_2_85} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.85

ITA_TINIEE_85:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_85} --p4_ee_2 ${P4_EE_2_85} --p4_ee_3 ${P4_EE_2_85} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.85

ITA_DINC_90:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_90} --p4_ee_2 ${P4_EE_2_90} --p4_ee_3 ${P4_EE_2_90} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.90

ITA_TINIEE_90:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_90} --p4_ee_2 ${P4_EE_2_90} --p4_ee_3 ${P4_EE_2_90} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.90

ITA_DINC_95:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_95} --p4_ee_2 ${P4_EE_2_95} --p4_ee_3 ${P4_EE_2_95} --p4_nf ${P4_NF} --topo Italian --sol DINC --th 0.95

ITA_TINIEE_95:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_95} --p4_ee_2 ${P4_EE_2_95} --p4_ee_3 ${P4_EE_2_95} --p4_nf ${P4_NF} --topo Italian --sol TINIEE --th 0.95

ITA_NNsplit:
	sudo python3 network.py --p4_ee_1 ${No_EE_1} --p4_ee_2 ${No_EE_2} --p4_ee_3 ${P4_EE_3} --p4_nf ${P4_NF} --topo Italian --sol NN --th 0.55

JPN_TINIEE_55:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_55} --p4_ee_2 ${P4_EE_2_55} --p4_ee_3 ${P4_EE_2_55} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.55

JPN_DINC_55:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_55} --p4_ee_2 ${P4_EE_2_55} --p4_ee_3 ${P4_EE_2_55} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.55

JPN_TINIEE_60:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_60} --p4_ee_2 ${P4_EE_2_60} --p4_ee_3 ${P4_EE_2_60} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.60

JPN_DINC_60:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_60} --p4_ee_2 ${P4_EE_2_60} --p4_ee_3 ${P4_EE_2_60} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.60

JPN_DINC_65:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_65} --p4_ee_2 ${P4_EE_2_65} --p4_ee_3 ${P4_EE_2_65} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.65

JPN_TINIEE_65:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_65} --p4_ee_2 ${P4_EE_2_65} --p4_ee_3 ${P4_EE_2_65} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.65
JPN_DINC_70:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_70} --p4_ee_2 ${P4_EE_2_70} --p4_ee_3 ${P4_EE_2_70} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.70

JPN_TINIEE_70:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_70} --p4_ee_2 ${P4_EE_2_70} --p4_ee_3 ${P4_EE_2_70} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.70
JPN_DINC_75:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_75} --p4_ee_2 ${P4_EE_2_75} --p4_ee_3 ${P4_EE_2_75} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.75

JPN_TINIEE_75:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_75} --p4_ee_2 ${P4_EE_2_75} --p4_ee_3 ${P4_EE_2_75} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.75

JPN_DINC_80:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_80} --p4_ee_2 ${P4_EE_2_80} --p4_ee_3 ${P4_EE_2_80} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.80

JPN_TINIEE_80:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_80} --p4_ee_2 ${P4_EE_2_80} --p4_ee_3 ${P4_EE_2_80} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.80

JPN_DINC_85:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_85} --p4_ee_2 ${P4_EE_2_85} --p4_ee_3 ${P4_EE_2_85} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.85

JPN_TINIEE_85:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_85} --p4_ee_2 ${P4_EE_2_85} --p4_ee_3 ${P4_EE_2_85} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.85

JPN_DINC_90:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_90} --p4_ee_2 ${P4_EE_2_90} --p4_ee_3 ${P4_EE_2_90} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.90

JPN_TINIEE_90:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_90} --p4_ee_2 ${P4_EE_2_90} --p4_ee_3 ${P4_EE_2_90} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.90

JPN_DINC_95:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_95} --p4_ee_2 ${P4_EE_2_95} --p4_ee_3 ${P4_EE_2_95} --p4_nf ${P4_NF} --topo Japanese --sol DINC --th 0.95

JPN_TINIEE_95:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_95} --p4_ee_2 ${P4_EE_2_95} --p4_ee_3 ${P4_EE_2_95} --p4_nf ${P4_NF} --topo Japanese --sol TINIEE --th 0.95

JPN_NNsplit:
	sudo python3 network.py --p4_ee_1 ${No_EE_1} --p4_ee_2 ${No_EE_2} --p4_ee_3 ${P4_EE_3} --p4_nf ${P4_NF} --topo Japanese --sol NN --th 0.55



NSF_TINIEE_55:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_55} --p4_ee_2 ${P4_EE_2_55} --p4_ee_3 ${P4_EE_2_55} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.55
NSF_DINC_55:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_55} --p4_ee_2 ${P4_EE_2_55} --p4_ee_3 ${P4_EE_2_55} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.55

NSF_TINIEE_60:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_60} --p4_ee_2 ${P4_EE_2_60} --p4_ee_3 ${P4_EE_2_60} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.60
NSF_DINC_60:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_60} --p4_ee_2 ${P4_EE_2_60} --p4_ee_3 ${P4_EE_2_60} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.60

NSF_TINIEE_65:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_65} --p4_ee_2 ${P4_EE_2_65} --p4_ee_3 ${P4_EE_2_65} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.65
NSF_DINC_65:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_65} --p4_ee_2 ${P4_EE_2_65} --p4_ee_3 ${P4_EE_2_65} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.65

NSF_TINIEE_70:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_70} --p4_ee_2 ${P4_EE_2_70} --p4_ee_3 ${P4_EE_2_70} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.70
NSF_DINC_70:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_70} --p4_ee_2 ${P4_EE_2_70} --p4_ee_3 ${P4_EE_2_70} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.70

NSF_TINIEE_75:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_75} --p4_ee_2 ${P4_EE_2_75} --p4_ee_3 ${P4_EE_2_75} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.75
NSF_DINC_75:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_75} --p4_ee_2 ${P4_EE_2_75} --p4_ee_3 ${P4_EE_2_75} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.75

NSF_TINIEE_80:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_80} --p4_ee_2 ${P4_EE_2_80} --p4_ee_3 ${P4_EE_2_80} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.80
NSF_DINC_80:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_80} --p4_ee_2 ${P4_EE_2_80} --p4_ee_3 ${P4_EE_2_80} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.80


NSF_TINIEE_85:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_85} --p4_ee_2 ${P4_EE_2_85} --p4_ee_3 ${P4_EE_2_85} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.85
NSF_DINC_85:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_85} --p4_ee_2 ${P4_EE_2_85} --p4_ee_3 ${P4_EE_2_85} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.85

NSF_TINIEE_90:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_90} --p4_ee_2 ${P4_EE_2_90} --p4_ee_3 ${P4_EE_2_90} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.90
NSF_DINC_90:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_90} --p4_ee_2 ${P4_EE_2_90} --p4_ee_3 ${P4_EE_2_90} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.90

NSF_TINIEE_95:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_95} --p4_ee_2 ${P4_EE_2_95} --p4_ee_3 ${P4_EE_2_95} --p4_nf ${P4_NF} --topo NSFNET --sol TINIEE --th 0.95
NSF_DINC_95:
	sudo python3 network.py --p4_ee_1 ${P4_EE_1_95} --p4_ee_2 ${P4_EE_2_95} --p4_ee_3 ${P4_EE_2_95} --p4_nf ${P4_NF} --topo NSFNET --sol DINC --th 0.95

NSF_NNsplit:
	sudo python3 network.py --p4_ee_1 ${No_EE_1} --p4_ee_2 ${No_EE_2} --p4_ee_3 ${No_EE_3} --p4_nf ${P4_NF} --topo NSFNET --sol NN --th 0.55

stop:
	sudo mn -c

clean: stop
	sudo rm -f *.pcap
	# rm -rf $(PCAP_DIR) $(LOG_DIR) $(RULE_DIR)/rule*
	sudo rm -rf $(PCAP_DIR) $(LOG_DIR)
	sudo rm -rf $(RESULT_DIR)/*
