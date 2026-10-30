from setuptools import setup

setup(
    name="TTA Panda Test",
    version="0.1.0",
    options={
        "build_apps": {
            "application_id": "com.puffsco.ttatest",
            "android_version_code": 1,
            "android_abis": ["arm64-v8a"],
            "gui_apps": {"ttatest": "main.py"},
            "platforms": ["android"],
            "plugins": ["pandagles2"],
            "use_optimized_wheels": False,
        },
        "bdist_apps": {
            "installers": {"android": ["aab"]},
        },
    },
)
