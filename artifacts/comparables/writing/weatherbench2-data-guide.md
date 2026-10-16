---
author: "WeatherBench 2 team (Rasp et al.)"
org: "Google Research"
url: "https://weatherbench2.readthedocs.io/en/latest/data-guide.html"
date: "living doc"
fetch_date: "2026-10-15"
connects_to: "DeepMind (Lam, Price), Aurora, Jua, Silurian, Brightband, NVIDIA Earth-2"
why_it_matters: "Defines the ground truth, baselines and evaluation conventions that make a weather-model comparison fair (e.g. IFS HRES scored against its own analysis)."
---

```
import xarray as xr
```

# WeatherBench 2 Data Guide

One core part of WeatherBench 2 are ready-to-use, cloud-based datasets. This page lists and describes all the available datasets.

The datasets are stored in this public Google Cloud bucket: `gs://weatherbench2/datasets`.

**Please also check the LICENSE files for each dataset in the respective GCS buckets.** Some datasets allow commercial use. Others only permit research use.

## A note on resolutions

We provide the datasets at different resolutions. All files will have the number of longitude X latitude grid points in their filename, e.g. `64x32`. For the WeatherBench 2 paper, all evaluation was done at `240x121` = 1.5 degree resolution. All datasets were regridded using first-order conservative regridding, i.e., with weights proportional to the area of overlap between grid cells on the original and desired grids.

The `1440x721` (= 0.25 degrees) and `240x121` files contain the poles, i.e. -90 and 90 degree latitude, denoted with `with_poles`. `64x32` files do not contain the poles to ensure equal spacing.

## Ground-truth datasets

### ERA5

Our ERA5 datasets were downloaded from the Copernicus Climate Data Store and have a time range from 1959 to 2023 (incl.). The data here have been downsampled to 6h and 13 levels, even though a raw hourly dataset with 37 levels is also available at `gs://weatherbench2/datasets/era5/1959-2023_01_10-full_37-1h-0p25deg-chunk-1.zarr`

Location: `gs://weatherbench2/datasets/era5/`

Files:

* `1959-2023_01_10-full_37-1h-0p25deg-chunk-1.zarr`
* `1959-2023_01_10-wb13-6h-1440x721_with_derived_variables.zarr`
* `1959-2023_01_10-6h-240x121_equiangular_with_poles_conservative.zarr`
* `1959-2023_01_10-6h-64x32_equiangular_conservative.zarr`

*Note: Older version of the ERA5 files exist in the bucket to ensure continuity.*

See output below for a list of variables. The file also contains several derived variables which were computed using these methods.

```
xr.open_zarr('gs://weatherbench2/datasets/era5/1959-2023_01_10-wb13-6h-1440x721_with_derived_variables.zarr')
```

```
<xarray.Dataset>
Dimensions:                                           (time: 93544,
                                                       latitude: 721,
                                                       longitude: 1440,
                                                       level: 13)
Coordinates:
  * latitude                                          (latitude) float32 90.0...
  * level                                             (level) int64 50 ... 1000
  * longitude                                         (longitude) float32 0.0...
  * time                                              (time) datetime64[ns] 1...
Data variables: (12/62)
    10m_u_component_of_wind                           (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    10m_v_component_of_wind                           (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    10m_wind_speed                                    (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    2m_dewpoint_temperature                           (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    2m_temperature                                    (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    above_ground                                      (time, level, latitude, longitude) float32 dask.array<chunksize=(1, 13, 721, 1440), meta=np.ndarray>
    ...                                                ...
    volumetric_soil_water_layer_1                     (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    volumetric_soil_water_layer_2                     (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    volumetric_soil_water_layer_3                     (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    volumetric_soil_water_layer_4                     (time, latitude, longitude) float32 dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>
    vorticity                                         (time, level, latitude, longitude) float32 dask.array<chunksize=(1, 13, 721, 1440), meta=np.ndarray>
    wind_speed                                        (time, level, latitude, longitude) float32 dask.array<chunksize=(1, 13, 721, 1440), meta=np.ndarray>
```

xarray.Dataset

* Dimensions:

  + time: 93544
  + latitude: 721
  + longitude: 1440
  + level: 13
* Coordinates: (4)

  + latitude

    (latitude)

    float32

    90.0 89.75 89.5 ... -89.75 -90.0

    **long\_name :**:   latitude
    **units :**:   degrees\_north

    ```
    array([ 90.  ,  89.75,  89.5 , ..., -89.5 , -89.75, -90.  ], dtype=float32)
    ```
  + level

    (level)

    int64

    50 100 150 200 ... 700 850 925 1000

    ```
    array([  50,  100,  150,  200,  250,  300,  400,  500,  600,  700,  850,  925,
           1000])
    ```
  + longitude

    (longitude)

    float32

    0.0 0.25 0.5 ... 359.2 359.5 359.8

    **long\_name :**:   longitude
    **units :**:   degrees\_east

    ```
    array([0.0000e+00, 2.5000e-01, 5.0000e-01, ..., 3.5925e+02, 3.5950e+02,
           3.5975e+02], dtype=float32)
    ```
  + time

    (time)

    datetime64[ns]

    1959-01-01 ... 2023-01-10T18:00:00

    ```
    array(['1959-01-01T00:00:00.000000000', '1959-01-01T06:00:00.000000000',
           '1959-01-01T12:00:00.000000000', ..., '2023-01-10T06:00:00.000000000',
           '2023-01-10T12:00:00.000000000', '2023-01-10T18:00:00.000000000'],
          dtype='datetime64[ns]')
    ```
* Data variables: (62)

  + 10m\_u\_component\_of\_wind

    (time, latitude, longitude)

    float32

    dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>

    **long\_name :**:   10 metre U wind component
    **short\_name :**:   u10
    **units :**:   m s\*\*-1

    |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | |  | Array | Chunk | | --- | --- | --- | | Bytes | 361.80 GiB | 3.96 MiB | | Shape | (93544, 721, 1440) | (1, 721, 1440) | | Dask graph | 93544 chunks in 2 graph layers | | | Data type | float32 numpy.ndarray | | |  |
  + 10m\_v\_component\_of\_wind

    (time, latitude, longitude)

    float32

    dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>

    **long\_name :**:   10 metre V wind component
    **short\_name :**:   v10
    **units :**:   m s\*\*-1

    |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | |  | Array | Chunk | | --- | --- | --- | | Bytes | 361.80 GiB | 3.96 MiB | | Shape | (93544, 721, 1440) | (1, 721, 1440) | | Dask graph | 93544 chunks in 2 graph layers | | | Data type | float32 numpy.ndarray | | |  |
  + 10m\_wind\_speed

    (time, latitude, longitude)

    float32

    dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>

    |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | |  | Array | Chunk | | --- | --- | --- | | Bytes | 361.80 GiB | 3.96 MiB | | Shape | (93544, 721, 1440) | (1, 721, 1440) | | Dask graph | 93544 chunks in 2 graph layers | | | Data type | float32 numpy.ndarray | | |  |
  + 2m\_dewpoint\_temperature

    (time, latitude, longitude)

    float32

    dask.array<chunksize=(1, 721, 1440), meta=np.ndarray>

    **long\_name :**:   2 metre dewpoint temperature
    **short\_name :**:   d2m

[Excerpt truncated at the line cap; see url for the remainder.]
