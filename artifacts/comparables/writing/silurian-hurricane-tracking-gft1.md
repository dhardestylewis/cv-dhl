---
author: "Silurian"
org: "Silurian"
url: "https://silurian.ai/blog/accurate-hurricane-tracking-with-gft1"
date: "2024-09-15"
fetch_date: "2026-10-15"
connects_to: "Gupta, Shankar (Silurian)"
why_it_matters: "Case-study style result: specific events, named baseline (government forecasts), and a stated metric."
---

Tropical storms and hurricanes are some of the most visible and impactful features of the Earth’s weather system. Predicting their paths early and accurately allows businesses and governments to adequately prepare, save lives, and minimize losses.

Here, we briefly showcase early results using our first medium-range AI weather forecasting model - the Generative Forecasting Transformer (GFT1) - to predict recent storm tracks. We computed re-forecasts from operational initial conditions for several major storms in the ongoing 2024 season: Beryl, Francine, Neville, Debby, Ernesto, and Ewiniar. We chose these storms because they have long, relatively complex tracks and either made landfall or had a significant chance of doing so.

We compare the GFT1 re-forecasts to operational forecasts from the high-resolution HRES model. HRES is the widely respected, flagship, medium-range model from the European Centre for Medium-Range Weather Forecasts (ECMWF). We use IBTrACS records as the true tracks for each storm. None of these storms were present in GFT's training data, which excludes all of 2023 and 2024. Furthermore, the model has not been rollout-finetuned.

Animated wind speed at 10 meter height for the GFT1 forecast of Hurricane Beryl intialized at 7 pm EST on July 1st. The GFT1 forecasted cyclone is clear as it moves over the Yucatan Peninsula, across the Gulf, and into Texas. The HRES forecast initialized at this time shows the storm moving into northern Mexico instead.

GFT1 performs well, with notable superiority forecasting the tracks of Beryl, Neville, and Debby. As the GFT model improves, we expect it to be an important source of independent forecasts, alongside traditional models, and achieve clear superiority in the near future. To have a closer look at some of these forecasts, you can use our interactive visualisation tool at hurricanes2024.silurian.ai.

## Beryl

Hurricane Beryl formed earlier in the season than any other Category 5 Atlantic hurricane on record, making it a genuine outlier and a compelling test for data-driven, AI weather forecasting models. It caused severe and widespread damage in the Caribbean islands and eventually made landfall on the Gulf Coast of Texas as a Category 1 hurricane. It caused floods, wind damage, and a reported 36 deaths in the Houston area.

Silurian’s GFT1 distinguishes itself by forecasting the approximate path of Hurricane Beryl roughly **three days** before the flagship HRES model. Late on July 1st (EST), the GFT1 forecast accurately tracks the hurricane’s path through the Gulf of Mexico and onto the coast of Texas. Only by July 5th did HRES capture the storm’s trajectory into the southern United States instead of Northern Mexico.

## Francine

At the time of this writing, Francine is the latest hurricane to impact the Gulf Coast of the United States. Francine made landfall on September 11 in Louisiana, causing extensive flooding and widespread power outages. While the GFT forecast stays closer to the true path for most of the time, both models predicted a landfall further west than the actual landfall location.

Animated wind speed at 10 meter height for the GFT1 forecast of Hurricane Francine.

## Debby

Debby achieved Category 1 status on August 5th before making landfall over Florida, then turned North over the mid-Atlantic coast. In this case, HRES, picks up the northward turn, but fails to capture the storm's path later on. In contrast, GFT accurately predicts the northern trajectory of the storm.

Animated wind speed at 10 meter height for the GFT1 forecast of Hurricane Debby. GFT1 accurately captures the northern turn of the hurricane and its subsequent path.

## Neville

Severe Tropical Cyclone Neville formed in the Indian Ocean after spending two weeks as a tropical low traversing the eastern Indian Ocean. Neville eventually moved steadily westward away from the Australian mainland, posing no direct threat to land areas, as GFT also predicted. However, HRES predicted a turn towards Australia, which did not happen.

Animated wind speed at 10 meter height for the GFT1 forecast of Neville. GFT1 correctly forecasts the westward turn of the storm. In contrast, HRES wrongly predicts a trajectory towards Australia. Cyclone Megan can also be seen developing at the same time along the coast of Northern Australia.

## Ernesto

Ernesto intensified into a tropical storm on August 12th and, two days later, into a Category 1 hurricane. The storm caused flooding and widespread power outages in Puerto Rico and throughout the Caribbean. Here again, GFT1 correctly predicts Ernesto’s general track. HRES, in contrast, predicts a sharper northeastern turn towards the end, which deviates from the storm’s actual path.

Animated wind speed at 10 meter height for the GFT1 forecast of Hurricane Ernesto. In this case, the models perform relatively similarly, with GFT1 performing slightly better in predicting the late stages of the track.

## Ewiniar

Typhoon Ewiniar was a significant tropical cyclone that formed in May 2024 as the first named storm and typhoon of this year's Pacific typhoon season. The storm affected the Philippines, Japan, and Alaska, causing 6 fatalities, 8 injuries, and approximately $20.9 million in damages. Here, we see both models deviating slightly from the true path as the storm traverses the Philippine Sea.

Animated wind speed at 10 meter height for the GFT1 forecast of Typhoon Ewiniar. Both models perform similarly in this case.

## Ensemble Forecasts

There is a lot of inherent uncertainty in forecasting the path of tropical storms and hurricanes. To capture this uncertainty, meteorologists typically use an ensemble forecast, as opposed to a single forecast. The spread of the ensemble members gives an idea of the range of possible outcomes. As an early look at the ensemble forecasting capabilities of GFT1, we show an ensemble forecast for Hurricane Beryl.

We compare this ensemble forecast with the forecasted "cone" of trajectories from NOAA and National Weather Service (NWS), with both ensembles initialized at identical times. The official NOAA/NWS is shown immediately below, followed by the GFT ensemble. Like the HRES forecast, the US government cone weights Mexico-bound trajectories heavily. The GFT1 ensemble, however, is nicely distributed around the true, future path of the storm as it bends northward towards Texas. This is only one instance, of course, but it is a very encouraging sign of the model's capacity to accurately forecast distributions for hurricanes and other rare events.

> NOAA/NWS forecast cone for Hurricane Beryl. The cone is heavily weighted towards Mexico. Source: NOAA/NWS

> GFT1 ensemble forecast for Hurricane Beryl. The ensemble is concentrated further north than the NOAA hurricane cone.

## What's next

Despite the observational records containing relatively few accurate examples of tropical storms and even fewer examples of the strongest storms like Hurricane Beryl, Silurian’s GFT1 shows signs of improved performance on rare and impactful events. The model is able to capture patterns in the Earth's atmosphere that allows it to predict the path of the storms with a higher degree of accuracy.

We are working on more robust evaluations of model performance on hurricanes by including more storms, other key variables like wind speed, and probabilistic ensemble forecasts. We are also in the process of expanding evaluations to other rare events like temperature extremes.

If you would like to hear more, you can reach us at contact@silurian.ai

## From Forecast to Action

Talk to us about a deployment. See proof across energy and government.

book a demo

A team of researchers and engineers from:
