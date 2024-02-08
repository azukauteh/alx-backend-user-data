#!/usr/bin/env python3
"""Hashing with bcrypt"""
import bcrypt


def hash_password(password):
    """
    Hashes the password using bcrypt.
    """
    """ Generate a salt and hash the password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
