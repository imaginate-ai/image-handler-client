import pytest
from image_handler_client.schemas.image_info import ImageInfo, ImageStatus, IMAGE_INFO_SCHEMA


def test_image_info_creation():
    # Test creating an ImageInfo instance
    image_info = ImageInfo(
        filename="test_image.jpg",
        date="2024-07-29",
        theme="wildlife",
        real=True,
        status=ImageStatus.VERIFIED
    )
    assert image_info.filename == "test_image.jpg"
    assert image_info.date == "2024-07-29"
    assert image_info.theme == "wildlife"
    assert image_info.real is True
    assert image_info.status == ImageStatus.VERIFIED


def test_image_info_default_status():
    # Test creating an ImageInfo instance with default status
    image_info = ImageInfo(
        filename="test_image.jpg",
        date="2024-07-29",
        theme="wildlife",
        real=True
    )
    assert image_info.status == ImageStatus.UNVERIFIED


def test_image_info_schema_load():
    # Test loading data into ImageInfoSchema
    data = {
        "filename": "test_image.jpg",
        "date": "2024-07-29",
        "theme": "wildlife",
        "real": True,
        "status": "verified"
    }
    result = IMAGE_INFO_SCHEMA.load(data)
    assert result.filename == "test_image.jpg"
    assert result.date == "2024-07-29"
    assert result.theme == "wildlife"
    assert result.real is True
    assert result.status == ImageStatus.VERIFIED


def test_image_info_schema_load_default_status():
    # Test loading data into ImageInfoSchema without status
    data = {
        "filename": "test_image.jpg",
        "date": "2024-07-29",
        "theme": "wildlife",
        "real": True
    }
    result = IMAGE_INFO_SCHEMA.load(data)
    assert result.filename == "test_image.jpg"
    assert result.date == "2024-07-29"
    assert result.theme == "wildlife"
    assert result.real is True
    assert result.status == ImageStatus.UNVERIFIED


def test_image_info_schema_dump():
    # Test dumping ImageInfo instance to dictionary
    image_info = ImageInfo(
        filename="test_image.jpg",
        date="2024-07-29",
        theme="wildlife",
        real=True,
        status=ImageStatus.VERIFIED
    )
    result = IMAGE_INFO_SCHEMA.dump(image_info)
    expected = {
        "filename": "test_image.jpg",
        "date": "2024-07-29",
        "theme": "wildlife",
        "real": True,
        "status": "verified"
    }
    assert result == expected


def test_image_info_schema_load_invalid_status():
    # Test loading data with invalid status
    data = {
        "filename": "test_image.jpg",
        "date": "2024-07-29",
        "theme": "wildlife",
        "real": True,
        "status": "invalid_status"
    }
    with pytest.raises(ValueError):
        IMAGE_INFO_SCHEMA.load(data)
