import pydicom
from pydicom import FileDataset


def p_dicom(ds: FileDataset, field: str):
    print(f"{field}: {ds[field].value}")


def show_presentation(ds: FileDataset):
    """
    The fields I'm using here I found with ds.dir() this way:
    ds.dir('id') -> [
        'DeidentificationMethod', 'DeidentificationMethodCodeSequence',
        'DetectorID', 'FrameOfReferenceUID', 'Grid', 'PatientID', 'PatientIdentityRemoved',
        'SOPClassUID', 'SOPInstanceUID', 'SeriesInstanceUID', 'StudyID', 'StudyInstanceUID',
        'WindowWidth',
    ]
    ds.dir('number') -> [
        'AccessionNumber', 'DeviceSerialNumber', 'InstanceNumber', 'SeriesNumber',
    ]
    """
    p_dicom(ds, "PatientID")
    p_dicom(ds, "StudyID")
    p_dicom(ds, "SOPClassUID")
    p_dicom(ds, "SOPInstanceUID")
    p_dicom(ds, "SeriesInstanceUID")
    p_dicom(ds, "StudyInstanceUID")
    p_dicom(ds, "InstanceNumber")
    p_dicom(ds, "SeriesNumber")


# Carregar imagens
original = pydicom.dcmread("image_processing/images/mammography.dcm")
modified = pydicom.dcmread("image_processing/images/mammography_modified.dcm")

print("Original:")
show_presentation(original)

print("Modified:")
show_presentation(modified)
