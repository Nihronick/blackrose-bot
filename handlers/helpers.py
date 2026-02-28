import logging
from aiogram import F, Router, types
from aiogram.exceptions import TelegramBadRequest

logger = logging.getLogger(__name__)

router = Router()


@router.message(F.video)
async def get_video_id(message: types.Message):
    video = message.video
    await message.answer(
        f"🎥 <b>VIDEO File ID:</b>\n<code>{video.file_id}</code>\n\n"
        f"📊 Размер: {video.file_size / (1024*1024):.2f} MB\n"
        f"⏱ Длительность: {video.duration} сек",
        parse_mode="HTML"
    )


@router.message(F.document)
async def get_document_id(message: types.Message):
    doc = message.document
    await message.answer(
        f"📁 <b>DOCUMENT File ID:</b>\n<code>{doc.file_id}</code>\n\n"
        f"📄 Имя: {doc.file_name}\n"
        f"📊 Размер: {doc.file_size / (1024*1024):.2f} MB\n"
        f"🔖 Тип: {doc.mime_type or 'unknown'}",
        parse_mode="HTML"
    )


@router.message(F.photo)
async def get_photo_id(message: types.Message):
    photo = message.photo[-1]
    await message.answer(
        f"📸 <b>PHOTO File ID:</b>\n<code>{photo.file_id}</code>\n\n"
        f"📊 Размер: {photo.file_size / 1024:.2f} KB\n"
        f"📐 {photo.width}x{photo.height}",
        parse_mode="HTML"
    )


@router.message(F.animation)
async def get_animation_id(message: types.Message):
    anim = message.animation
    await message.answer(
        f"🎬 <b>GIF File ID:</b>\n<code>{anim.file_id}</code>\n\n"
        f"📊 Размер: {anim.file_size / (1024*1024):.2f} MB",
        parse_mode="HTML"
    )