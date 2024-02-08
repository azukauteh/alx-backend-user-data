#!/usr/bin/env python3
"""Hashing with bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
