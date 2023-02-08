from model_bakery import baker


def test_github_properties(library):
    properties = library.github_properties()
    assert properties["owner"] == "boostorg"
    assert properties["repo"] == "multi_array"


def test_github_owner(library):
    assert library.github_owner == "boostorg"


def test_github_repo(library):
    assert library.github_repo == "multi_array"


def test_category_creation(category):
    assert category.name is not None


def test_library_creation(library):
    assert library.versions.count() == 0


def test_issue_creation(issue, library):
    assert issue.library == library


def test_pull_request_creation(pull_request, library):
    assert pull_request.library == library


def test_library_version_creation(library_version, library, version):
    assert library_version.library == library
    assert library_version.version == version


def test_library_version_str(library_version, library, version):
    assert str(library_version) == f"{library.name} ({version.name})"


def test_library_version_multiple_versions(library, library_version):
    assert library.versions.count() == 1
    assert library.versions.filter(
        library_version__version=library_version.version
    ).exists()
    other_version = baker.make("versions.Version", name="New Version")
    new_library_version = baker.make(
        "libraries.LibraryVersion", library=library, version=other_version
    )
    assert library.versions.count() == 2
    assert library.versions.filter(
        library_version__version=library_version.version
    ).exists()
    assert library.versions.filter(library_version__version=other_version).exists()
