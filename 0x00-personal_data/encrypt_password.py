#!/usr/bin/env python3
"""Hashing with bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password, password):
    """
    Validates the provided password against the hashed password using bcrypt.
    """
    """ Check if the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
