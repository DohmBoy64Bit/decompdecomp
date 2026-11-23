"""Regression test for the preserved IDO 5.3 C++ IRIX compiler archive.

The older ido5.3_c++.tar.xz URL returns 404. The preserved cfront archive
has been verified against the publisher's Git blob identity, and the SHA-256
below was computed from that same archive.
"""
from decompnet import toolchains


def test_ido_5_3_cxx_archive_url_and_checksum_are_pinned():
    compiler = toolchains.get("ido-5.3-cxx")
    parts = compiler.parts_for("linux-x86_64")
    assert len(parts) == 1
    archive = parts[0]
    url = "https://raw.githubusercontent.com/LLONSIT/qemu-irix-helpers/n/qemu/ido5.3_cfront.tar.xz"
    assert compiler.source == url
    assert archive["url"] == url
    assert archive["sha256"] == "18b40acdc7b7f7c4ef840245f3f0a62d6be8b92738eee77dc02e05f378fa6fc7"
    assert archive["platforms"] == ["linux-x86_64"]
