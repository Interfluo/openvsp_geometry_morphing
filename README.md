# OpenVSP Parametric Modeling Wrapper

https://user-images.githubusercontent.com/79390007/202881577-41a47f8e-ab9e-441c-a357-41053c462430.mp4

- This project is a collection of utilities for modifying parametrically defined openvsp geometries.
- For this to work correctly the directory structure and contents must be defined correctly (see set-up) and the openvsp model must be correctly defined with parameter links and design parameters (see video: **video**)


## Set-up

    ├───project
        ├───OpenVSP-3.30.0-win64
            ├───missile_generic
                ├───geometry.vsp3
                ├───parameters.des
                ├───script.vspscript
            ├───airplane_generic
                ├───geometry.vsp3
                ├───parameters.des
                ├───script.vspscript
            ├───vsp.exe
            └───etc...
        ├───venv
        ├───main.py
        └───README.md
