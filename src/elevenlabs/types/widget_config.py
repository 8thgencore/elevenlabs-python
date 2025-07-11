# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .embed_variant import EmbedVariant
from .widget_config_output_avatar import WidgetConfigOutputAvatar
from .widget_expandable import WidgetExpandable
from .widget_feedback_mode import WidgetFeedbackMode
from .widget_language_preset import WidgetLanguagePreset
from .widget_placement import WidgetPlacement
from .widget_styles import WidgetStyles
from .widget_text_contents import WidgetTextContents


class WidgetConfig(UncheckedBaseModel):
    variant: typing.Optional[EmbedVariant] = pydantic.Field(default=None)
    """
    The variant of the widget
    """

    placement: typing.Optional[WidgetPlacement] = pydantic.Field(default=None)
    """
    The placement of the widget on the screen
    """

    expandable: typing.Optional[WidgetExpandable] = pydantic.Field(default=None)
    """
    Whether the widget is expandable
    """

    avatar: typing.Optional[WidgetConfigOutputAvatar] = pydantic.Field(default=None)
    """
    The avatar of the widget
    """

    feedback_mode: typing.Optional[WidgetFeedbackMode] = pydantic.Field(default=None)
    """
    The feedback mode of the widget
    """

    bg_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The background color of the widget
    """

    text_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text color of the widget
    """

    btn_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The button color of the widget
    """

    btn_text_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The button text color of the widget
    """

    border_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The border color of the widget
    """

    focus_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The focus color of the widget
    """

    border_radius: typing.Optional[int] = pydantic.Field(default=None)
    """
    The border radius of the widget
    """

    btn_radius: typing.Optional[int] = pydantic.Field(default=None)
    """
    The button radius of the widget
    """

    action_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The action text of the widget
    """

    start_call_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start call text of the widget
    """

    end_call_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end call text of the widget
    """

    expand_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expand text of the widget
    """

    listening_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text to display when the agent is listening
    """

    speaking_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text to display when the agent is speaking
    """

    shareable_page_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text to display when sharing
    """

    shareable_page_show_terms: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to show terms and conditions on the shareable page
    """

    terms_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text to display for terms and conditions
    """

    terms_html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTML to display for terms and conditions
    """

    terms_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key to display for terms and conditions
    """

    show_avatar_when_collapsed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to show the avatar when the widget is collapsed
    """

    disable_banner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to disable the banner
    """

    override_link: typing.Optional[str] = pydantic.Field(default=None)
    """
    The override link for the widget
    """

    mic_muting_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable mic muting
    """

    transcript_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the widget should show the conversation transcript as it goes on
    """

    text_input_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user should be able to send text messages
    """

    text_contents: typing.Optional[WidgetTextContents] = pydantic.Field(default=None)
    """
    Text contents of the widget
    """

    styles: typing.Optional[WidgetStyles] = pydantic.Field(default=None)
    """
    Styles for the widget
    """

    language_selector: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to show the language selector
    """

    supports_text_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the widget can switch to text only mode
    """

    custom_avatar_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The custom avatar path
    """

    language_presets: typing.Optional[typing.Dict[str, WidgetLanguagePreset]] = pydantic.Field(default=None)
    """
    Language presets for the widget
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
