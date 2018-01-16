package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewEditCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "edit",
      Short: "Edit a task",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Edit command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
