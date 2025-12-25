# %% [markdown]
# # app

# %%
#|default_exp cli.app

# %%
#|hide
from nblite import nbl_export, show_doc; nbl_export()

# %%
#|export
import typer

# %%
#|export
app = typer.Typer(invoke_without_command=True)
