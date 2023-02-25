from voluptuous import Schema, PREVENT_EXTRA

create_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

create_update_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

register_user = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

unregister_user = Schema(
    {
        "error": str
    },
    required=True,
    extra=PREVENT_EXTRA
)