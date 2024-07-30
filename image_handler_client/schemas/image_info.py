from dataclasses import dataclass
from enum import Enum
from typing import Optional
from marshmallow import Schema, fields, post_load, post_dump


class ImageStatus(Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    REJECTED = "rejected"


@dataclass(frozen=True)
class ImageInfo:
    filename: str
    date: str
    theme: str
    real: bool
    status: Optional[ImageStatus] = ImageStatus.UNVERIFIED


class ImageInfoSchema(Schema):
    filename = fields.Str(required=True)
    date = fields.Str(required=True)
    theme = fields.Str(required=True)
    real = fields.Bool(required=True)
    status = fields.Field(required=False, load_default=ImageStatus.UNVERIFIED.value)

    @post_load
    def make_image_info(self, data, **kwargs):
        data['status'] = ImageStatus(data['status'])
        return ImageInfo(**data)

    @post_dump
    def convert_status_to_str(self, data, **kwargs):
        if 'status' in data and isinstance(data['status'], ImageStatus):
            data['status'] = data['status'].value
        return data


IMAGE_INFO_SCHEMA = ImageInfoSchema()
