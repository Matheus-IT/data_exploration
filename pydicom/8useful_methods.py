import pydicom


with pydicom.dcmread("pydicom/image5.dcm") as ds:
    print(ds.group_dataset(0x0010))
    print(ds.dir("Patient"))
