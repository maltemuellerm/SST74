# Sea Surface Temperature Simulation in Ocean and Weather models
## Project SST-74 Romsenter 2023-2025
## Repository for

* **Verification** of AROME Arctic - GOTM and BarentsRoms (buoys and satellite data)
* **SkinTemperature** Simple model / Observation Operators for SST skin and subskin temperature

## Getting started

- Verification: 
	- Analyse_Buoy_AROME+GOTM.ipynb - Extracts trajectories from AROME output following preselected trajectories

- SkinTemperature 
	- SST_model_ZB,ipynb - a prognostic scheme of sea skin temperature by Zeng & Beljaars 2005. This implementation reads atmospheric forcing files obtained from AROME Arctic along a specified trajectory (Analyse_Buoy_AROME+GOTM.ipynb) 		
 	- SSTmodel_new - Uses SST  model is described in [Börner et al. (2022)](https://arxiv.org/abs/2205.07933)
