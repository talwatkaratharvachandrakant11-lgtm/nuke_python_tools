import nuke

# =============================================
# 1. CUSTOM WRITE NODE
# =============================================
def create_custom_write_node():
    """
    Creates a custom Write node with pre-configured output path
    based on shot information (project, sequence, shot, version)
    """
    # Default values - can be customized per project
    project = "myProject"
    sequence = "sq010"
    shot = "sh0010"
    version = "v01"
    
    # Build file path
    file_path = "/path/to/{}/sequences/{}/{}/{}/render/{}.####.exr".format(
        project, sequence, shot, version, shot
    )
    
    # Create Write node
    write_node = nuke.createNode("Write")
    write_node["file"].setValue(file_path)
    write_node["file_type"].setValue("exr")
    write_node["colorspace"].setValue("linear")
    
    return write_node

# Add to Nuke menu
nuke.menu("Nodes").addCommand("Custom/Custom Write Node", lambda: create_custom_write_node())

# =============================================
# 2. SPLIT EXR CHANNELS
# =============================================
def split_exr_channels():
    """
    Creates multiple shuffle nodes from a multi-channel EXR file
    Splits each layer into individual nodes
    """
    selected_node = nuke.selectedNode()
    if not selected_node or selected_node.Class() != "Read":
        nuke.message("Please select a Read node with an EXR file.")
        return

    channels = selected_node.channels()
    layers = list(set([c.split('.')[0] for c in channels]))
    
    for layer in layers:
        shuffle_node = nuke.createNode("Shuffle")
        shuffle_node.setInput(0, selected_node)
        shuffle_node["in"].setValue(layer)
        shuffle_node["out"].setValue("rgb")
        shuffle_node["label"].setValue("[value in]")

# Add to Nuke menu
nuke.menu("Nuke").addCommand("Utilities/Split EXR", split_exr_channels)

# =============================================
# 3. SCRIPT CLEANUP TOOL
# =============================================
def cleanup_script():
    """
    Cleans up Nuke script by:
    - Removing unnecessary nodes
    - Deleting error nodes
    - Disabling unused branches
    - Optimizing node graph
    """
    # Remove nodes with errors
    for node in nuke.allNodes():
        if node.hasError():
            nuke.delete(node)
    
    # Remove unnecessary node types
    unnecessary_classes = ["NoOp", "Viewer", "BackdropNode"]
    for node in nuke.allNodes():
        if node.Class() in unnecessary_classes:
            nuke.delete(node)
    
    # Disable unused branches (no connections on output)
    for node in nuke.allNodes():
        if not node.dependent() and node.Class() not in ["Viewer", "Write"]:
            node["disable"].setValue(True)
    
    nuke.message("Script cleanup completed.")

# Add to Nuke menu
nuke.menu("Nuke").addCommand("Utilities/Cleanup Script", cleanup_script)

print("Nuke Python Assignment Tools loaded successfully!")