package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewShowCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "show",
      Short: "Show a task",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Edit command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
